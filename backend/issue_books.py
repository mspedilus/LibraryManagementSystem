from datetime import datetime
from sql_connection import get_sql_connection

#Inserts new book rental
def insert_Issued_Books(connection, order):
    cursor = connection.cursor()
    query1 = ("INSERT INTO issued_books (issued_id, reader_id, first_name, last_name, number_of_books, date_issued, date_returned) VALUES (%s, %s, %s, %s, %s, %s, %s)")
    orderData = (order['issued_id'],  order['reader_id'], order['first_name'],  order['last_name'], order['number_of_books'], datetime.now(), datetime.now())
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


# def get_all_orders(connection):
#     cursor = connection.cursor()
#     query = ("SELECT * FROM orders")
#     cursor.execute(query)

#     response = []
#     for (order_id, customer_name, total, datetime) in cursor:
#         response.append({
#             'order_id': order_id,
#             'customer_name': customer_name,
#             'total': total,
#             'datetime': datetime
#         })
        
#     return response    

if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_Issued_Books(connection, {
            'issued_id': '123456',
            'reader_id': '1',
            'first_name': 'James',
            'last_name': 'Darner',
            "number_of_books": "2",
            'books': [
                {
                    'ISBN': 212,
                    'book_title': "Twilight",
                    "author_name": "Dance",
                    "quantity": "1"
                },
                {
                    'ISBN': 2456,
                    'book_title': "Outlander",
                    "author_name": "Dance",
                    "quantity": "1"
                }
            ]
        }))
    