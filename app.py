try:
    # Importing Flask and the configuration function
    from flask import Flask
    from configuration import configure_all
except ImportError as e:
    # In case of ImportError, print the error message and stop the execution
    print(f"Error: {e}")
    exit()

# Initialize the Flask application
app = Flask(__name__)

# Apply all configurations using the configure_all function
configure_all(app)

# Run the application if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
