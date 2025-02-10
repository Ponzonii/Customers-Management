# Import necessary modules and handle import errors
try:
    from flask import Blueprint as Bp, render_template as rt, request as req
    from Database.Models.customer import Customer
except ImportError as e:
    print(f"Error: {e}")
    exit()

# Create a Blueprint for customers routes
customers = Bp("customers", __name__)


# Route to list all customers
@customers.route("/list")
def list_customers():
    customers = Customer.select()
    return rt("list_customers.html", customers=customers)


# Route to insert a new customer
@customers.route("/new", methods=["POST"])
def new_customer():
    data = req.json

    # Check if email or phone number already exists
    if (
        Customer.select().where(Customer.email == data["email"]).exists()
        or Customer.select().where(Customer.phone == data["phone"]).exists()
    ):
        return (
            rt("error.html", error="Email ou número de telefone já cadastrados!"),
            400,
        )
    else:
        # Create a new customer
        new_customer = Customer.create(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            date_birth=data["dateBirth"],
        )
        return rt("item_customer.html", customer=new_customer)


# Route to display the form for creating a new customer
@customers.route("/form/new")
def form_new_customer():
    return rt("form_customer.html")


# Route to display the form for editing a customer
@customers.route("/<int:customer_id>/form/edit")
def form_edit_customer(customer_id):
    customer = Customer.get_by_id(customer_id)
    return rt("form_customer.html", customer=customer)


# Route to display customer details
@customers.route("/<int:customer_id>/details")
def details_customer(customer_id):
    customer = Customer.get_by_id(customer_id)
    return rt("detail_customer.html", customer=customer)


# Route to update a customer's information
@customers.route("/<int:customer_id>/update", methods=["PUT"])
def update_customer(customer_id):
    data = req.json
    customer = customer.get_by_id(customer_id)

    # Check if email or phone number already exists for another customer
    if (
        Customer.select()
        .where((Customer.email == data["email"]) & (Customer.id != customer_id))
        .exists()
    ) or (
        Customer.select()
        .where((Customer.phone == data["phone"]) & (Customer.id != customer_id))
        .exists()
    ):
        return rt("error.html", error="Email ou número de telefone já cadastrados!")
    else:
        # Update customer information
        customer.name = data["name"]
        customer.email = data["email"]
        customer.phone = data["phone"]
        customer.dateBirth = data["dateBirth"]
        customer.save()
        return rt("item_customer.html", customer=customer)


# Route to delete a customer
@customers.route("/<int:customer_id>/delete", methods=["DELETE"])
def delete_customer(customer_id):
    customer = Customer.delete_by_id(customer_id)
    return {"Successful": "ok"}
