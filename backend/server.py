import json
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import issue_books
import issue_fines
import books
import readers



connection = get_sql_connection()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/getAllBooks', methods=['GET'])
@cross_origin()
def getBooks():
    response = books.getAllBooks(connection)
    response = jsonify(response)
    return response


@app.route('/deleteBook', methods=['POST'])
@cross_origin()
def deleteBook():
    return_id = books.deleteBook(connection, request.form['book_id'])
    response = jsonify({
        'book_id': return_id
    })
    return response

@app.route('/insertBook', methods=['POST'])
@cross_origin()
def insertNewBook():
    payload = json.loads(request.form['data'])
    book_id = books.insertNewBook(connection, payload)
    print(book_id)
    response = jsonify({
        'book_id': book_id
    })
    return response

@app.route('/getAllReaders', methods=['GET'])
@cross_origin()
def getReaders():
    response = readers.getAllReaders(connection)
    response = jsonify(response)
    return response

@app.route('/deleteReader', methods=['POST'])
@cross_origin()
def deleteReader():
    return_id = readers.deleteReader(connection, request.form['reader_id'])
    response = jsonify({
        'reader_id': return_id
    })
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server for grocery management system")
    app.run(port=5000)