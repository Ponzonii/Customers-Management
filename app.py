try:
    from flask import Flask
    from configuration import configure_all
except ImportError as e:
    print(f"Error: {e}")
    exit()

app = Flask(__name__)

configure_all(app)

if __name__ == "__main__":
    app.run(debug=True)
