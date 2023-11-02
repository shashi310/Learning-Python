# # Import necessary modules
# from flask import Flask, render_template, request

# # Create an instance of the Flask class
# app = Flask(__name__)

# # Initialize an empty dictionary to store data
# data = {}

# # Define a route for the root URL "/"
# @app.route('/')
# def home():
#     return 'Welcome to my CRUD App!'

# # Define a route for creating entries
# @app.route('/create', methods=['GET', 'POST'])
# def create():
#     if request.method == 'POST':
#         key = request.form['key']
#         value = request.form['value']
#         data[key] = value
#         return f'Entry created: {key} - {value}'
#     return render_template('create.html')

# # Define a route for reading entries
# @app.route('/read')
# def read():
#     return str(data)

# # Define a route for updating entries
# @app.route('/update', methods=['GET', 'POST'])
# def update():
#     if request.method == 'POST':
#         key = request.form['key']
#         if key in data:
#             value = request.form['value']
#             data[key] = value
#             return f'Entry updated: {key} - {value}'
#         else:
#             return f'Entry with key {key} does not exist.'
#     return render_template('update.html')

# # Define a route for deleting entries
# @app.route('/delete', methods=['GET', 'POST'])
# def delete():
#     if request.method == 'POST':
#         key = request.form['key']
#         if key in data:
#             del data[key]
#             return f'Entry with key {key} deleted.'
#         else:
#             return f'Entry with key {key} does not exist.'
#     return render_template('delete.html')

# # This block of code ensures that the app runs only if this script is executed directly
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

data = {}

@app.route('/')
def home():
    return render_template('crud.html')

@app.route('/crud', methods=['POST', 'GET'])
def crud():
    if request.method == 'POST':
        action = request.form['action']

        if action == 'create':
            key = request.form['key']
            value = request.form['value']
            data[key] = value
            return f'Entry created: {key} - {value}'

        elif action == 'update':
            key = request.form['key']
            if key in data:
                value = request.form['value']
                data[key] = value
                return f'Entry updated: {key} - {value}'
            else:
                return f'Entry with key {key} does not exist.'

        elif action == 'delete':
            key = request.form['key']
            if key in data:
                del data[key]
                return f'Entry with key {key} deleted.'
            else:
                return f'Entry with key {key} does not exist.'

    elif request.method == 'GET':
        if request.args.get('action') == 'read':
            return str(data)

if __name__ == '__main__':
    app.run(debug=True)
