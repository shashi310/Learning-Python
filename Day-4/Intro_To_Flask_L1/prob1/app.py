# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route that handles requests to the root URL "/"
@app.route('/')
def welcome():
    # This function will be executed when the user visits the root URL
    return 'Welcome to my Greeting App!'

# Define a dynamic route that takes a username as a parameter
@app.route('/greet/<username>')
def greet_user(username):
    # This function takes the username from the URL and returns a greeting message
    return f'Hello, {username}!'

# Define another dynamic route for farewells
@app.route('/farewell/<username>')
def farewell_user(username):
    # This function takes the username from the URL and returns a farewell message
    return f'Goodbye, {username}!'

# This block of code ensures that the app runs only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)




# You can now go to http://localhost:5000/ to see the welcome message and try accessing the other routes like /greet/John and /farewell/John.