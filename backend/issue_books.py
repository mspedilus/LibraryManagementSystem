from datetime import datetime
from sql_connection import get_sql_connection

#Inserts new book rental
def insert_Issued_Books(connection, order):
    cursor = connection.cursor()
    query1 = ("INSERT INTO issued_books (issued_id, reader_id, first_name, last_name, number_of_books, date_issued, date_returned, due_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    orderData = (order['issued_id'],  order['reader_id'], order['first_name'],  order['last_name'], order['number_of_books'], datetime.now(), datetime.now(), datetime.now())
    cursor.execute(query1, orderData)


    issued_id = cursor.lastrowid
    query2 = ("INSERT INTO issued_books_details (issued_id, ISBN, book_title, author_name, quantity) VALUES (%s, %s, %s, %s, %s)")
    orderDetailsData = []
    for book in order['books']:
        orderDetailsData.append([
           issued_id, 
           book["ISBN"], 
           book["book_title"], 
           book["author_name"],
           book["quantity"]
        ])

    cursor.executemany(query2, orderDetailsData)

    connection.commit()
    return issued_id


def getAllIssuedBooks(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM issued_books")
    cursor.execute(query)

    response = []
    for (issued_id, reader_id, first_name, last_name, date_issued, date_returned, number_of_books ) in cursor:
        response.append({
            'issued_id': issued_id,
            'reader_id': reader_id,
            'first_name': first_name,
            'last_name': last_name,
            'date_issued': date_issued,
            'date_returned': date_returned,
            'number_of_books': number_of_books
        })
        
    return response    

if __name__ == '__main__':
    connection = get_sql_connection()

    