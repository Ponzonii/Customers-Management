// Utility functions for selecting elements
const $cru = (e) => document.querySelector(e), // Selects a single element
  $crus = (e) => document.querySelectorAll(e), // Selects multiple elements
  // Global configuration object
  $cruConfig = {
    prefix_url: "", // Base URL for requests
    headers: { "Content-Type": "application/json" }, // Default headers
    callbacks: {}, // Stores callback functions
  };

// Initialization function
const $C = (e = !1) => {
  if (e) for (let t of Object.keys(e)) $cruConfig[t] = e[t]; // Merge user-defined configurations
  $cruLoadEvents(); // Load event listeners
};

// Function to load all necessary event listeners
const $cruLoadEvents = () => {
  $cruLoadRequests(); // Attach AJAX request listeners
  $cruLoadFormIntercept(); // Attach form submission listeners
  $cruLoadAllContainers(); // Load dynamic content from `c-container` elements
};

// Loads a container marked with `c-container`
const $cruLoadContainer = async (e) => {
  e.classList.add("loaded"); // Prevent duplicate loading
  const t = e.closest("[c-container]") || e,
    r = t.getAttribute("c-container"), // URL to fetch data from
    c = t.getAttribute("c-target") || !1, // Target element to update
    a = t.getAttribute("c-type") || "html", // Response type
    n = t.getAttribute("c-callback") || !1, // Callback function name
    o = await fetch($cruConfig.prefix_url + r, {
      method: "GET",
      headers: $cruConfig.headers,
    }),
    s = await $cruTypeResponse(a, o), // Process response
    i = c ? $cru(c) : t;

  // Update target element if applicable
  (c || "off" != c) &&
    (c ? (i.innerHTML = s) : "html" == a && (i.innerHTML = s)),
    n && $cruConfig.callbacks[n](s, i), // Execute callback
    $cruLoadEvents(); // Reload event listeners
};

// Load all containers marked with `c-container`
const $cruLoadAllContainers = async () => {
  $crus("[c-container]:not(.loaded)").forEach(async (e) => {
    e.classList.add("loaded");
    $cruLoadContainer(e);
  });

  $crus("[c-reload]:not(.loaded)").forEach(async (e) => {
    e.classList.add("loaded");
    e.addEventListener("click", () => $cruLoadContainer(e));
  });
};

// Generic function to handle AJAX requests
const cruRequest = async (e, t) => {
  const r = e.getAttribute(`c-${t}`), // Request URL
    c = e.getAttribute("c-type") || "html", // Response type
    a = e.getAttribute("c-reload-container") || !1, // Reload container flag
    n = e.getAttribute("c-remove-closest") || !1, // Remove closest element
    o = e.getAttribute("c-self-remove") || !1, // Remove clicked element
    s = e.getAttribute("c-redirect") || !1, // Redirect URL
    i = e.getAttribute("c-swap") || !1, // Replace element with response
    d = e.getAttribute("c-append") || !1, // Append response content
    u = e.getAttribute("c-prepend") || !1, // Prepend response content
    l = e.getAttribute("c-callback") || !1, // Callback function name
    $ = e.getAttribute("c-target") || !1, // Target element to update
    g = await fetch($cruConfig.prefix_url + r, {
      method: t,
      headers: $cruConfig.headers,
    }),
    L = await $cruTypeResponse(c, g),
    f = !!$ && $cru($);

  // Perform actions based on attributes
  n && e.closest(n).remove();
  o && e.remove();
  i && ($cru(i).outerHTML = L);
  d && $cru(d).insertAdjacentHTML("beforeend", L);
  u && $cru(u).insertAdjacentHTML("afterbegin", L);
  a && $cruLoadContainer(e);
  f && (f.innerHTML = L);
  l && $cruConfig.callbacks[l](L, f);
  $cruLoadEvents();
  s && (window.location.href = s);
};

// Attach event listeners for AJAX requests
const $cruLoadRequests = () => {
  ["delete", "put", "get", "post"].forEach((method) => {
    $crus(`[c-${method}]:not(.loaded)`).forEach((e) => {
      e.classList.add("loaded");
      e.addEventListener("click", async () => cruRequest(e, method));
    });
  });
};

// Intercept form submissions and send AJAX requests instead
const $cruLoadFormIntercept = () => {
  $crus(".c-form:not(.loaded)").forEach((e) => {
    e.classList.add("loaded");
    e.addEventListener("submit", async (t) => {
      t.preventDefault(); // Prevent default form submission

      const r = e.getAttribute("action"),
        c = e.getAttribute("method").toUpperCase() || "POST",
        a = e.getAttribute("c-type") || "html",
        n = e.getAttribute("c-append") || !1,
        o = e.getAttribute("c-prepend") || !1,
        s = e.getAttribute("c-redirect") || !1,
        i = e.getAttribute("c-reset") || !1,
        d = e.getAttribute("c-swap") || !1,
        u = e.getAttribute("c-target") || !1,
        l = e.getAttribute("c-reload-container") || !1,
        $ = e.getAttribute("c-callback") || !1,
        g = $cruIsRead(c),
        L = Object.fromEntries(new FormData(t.target).entries()),
        f = cruFormatURL(r, g, L),
        b = await fetch(f, {
          method: c,
          headers: $cruConfig.headers,
          body: g ? null : JSON.stringify(L),
        }),
        p = await $cruTypeResponse(a, b);

      // Perform actions based on attributes
      d && ($cru(d).outerHTML = p);
      n && $cru(n).insertAdjacentHTML("beforeend", p);
      o && $cru(o).insertAdjacentHTML("afterbegin", p);
      u && ($cru(u).innerHTML = p);
      i && e.reset();
      l && $cruLoadContainer(e);
      $ && $cruConfig.callbacks[$]({ status: b.status, data: p }, e);
      $cruLoadEvents();
      s && (window.location.href = s);
    });
  });
};

// Utility functions
const $cruIsRead = (e) => ["GET", "HEAD"].includes(e);
const $cruTypeResponse = async (e, t) =>
  "html" == e ? await t.text() : await t.json();

// Initialize the script on page load
$C();
