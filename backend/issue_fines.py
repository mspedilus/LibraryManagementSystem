from datetime import datetime
from sql_connection import get_sql_connection

#Inserts new fine
def insert_Issued_Books(connection, order):
    cursor = connection.cursor()
    query = ("INSERT INTO issued_fines (issued_id, fine_id, reader_id, first_name, last_name, total, date_issued) VALUES (%s, %s, %s, %s, %s, %s, %s)")
    orderData = (order['issued_id'],  order['fine_id'], order['reader_id'], order['first_name'],  order['last_name'], order['total'], datetime.now())
    cursor.execute(query, orderData)
    connection.commit()
    return 

#Retreives all fines in issued_fines table
def getAllFines(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM issued_fines")
    cursor.execute(query)

    response = []
    for (issued_id, fine_id, reader_id, first_name, last_name, total, date_issued ) in cursor:
        response.append({
            'issued_id': issued_id,
            'fine_id': fine_id,
            'reader_id': reader_id,
            'first_name': first_name,
            'last_name': last_name,
            'date_issued': date_issued,
            'total': total
        })
        
    return response    

# #Deletes a fine from fine table
# def deleteFine(connection, fine_id):
#     cursor = connection.cursor()
#     query = ("DELETE FROM books WHERE book_id=" + str(fine_id))
#     cursor.execute(query)
#     connection.commit()
#     return

if __name__ == '__main__':
    connection = get_sql_connection()
    print(getAllFines(connection))
    # print(insert_Issued_Books(connection, {
    #         'issued_id': '123456',
    #         'reader_id': '1',
    #         'first_name': 'James',
    #         'last_name': 'Darner',
    #         "fine_id": "6451",
    #         "total": "150"
    #     }))
    