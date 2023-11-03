# i have first Installed Flask and Flask-RESTful with this command : 
# pip install Flask Flask-RESTful



from flask import Flask
from flask import request

from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Create a list of books as an example data source
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
]

# Define a request parser to parse incoming requests
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help='Title of the book')
parser.add_argument('author', type=str, help='Author of the book')

# Create a resource for handling book data
class BookResource(Resource):
    def post(self):
        args = parser.parse_args()
        new_book = {'id': len(books) + 1, 'title': args['title'], 'author': args['author']}
        books.append(new_book)
        return new_book, 201
    
    def get(self, book_id):
        return books[book_id - 1]

    def put(self, book_id):
      args = parser.parse_args()
      books[book_id - 1] = {'id': book_id, 'title': args['title'], 'author': args['author']}
      return books[book_id - 1], 201


    def delete(self, book_id):
        del books[book_id - 1]
        return '', 204

# Add the resource to the API with a URL route
api.add_resource(BookResource, '/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)

# now run the server
# python app.py

# then open postman , get req and delete is working but not post and put
