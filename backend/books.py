from sql_connection import get_sql_connection

#Retrieves all books in books table
def getAllBooks(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM books")
    cursor.execute(query)
    response = []

    for (ISBN, book_title, author_name, category, publisher, price, quantity, description) in cursor:
        response.append({
                'ISBN': ISBN, 
                'book_title': book_title, 
                'author_name': author_name,
                'category': category, 
                'publisher': publisher,
                'price': price,
                'quantity': quantity,
                "description": description
        })
    return response


#Inserts a new book into books table
def insertNewBook(connection, book):
    cursor = connection.cursor()
    query = ("INSERT INTO books (ISBN, book_title, author_name, category, publisher, price, quantity, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    data = (book['ISBN'], book['book_title'], book['author_name'], book['category'],
            book['publisher'], book['price'], book['quantity'], book['description'])
    cursor.execute(query, data)
    connection.commit()
    return


#Deletes a book from books table
def deleteBook(connection, book_id):
    cursor = connection.cursor()
    query = ("DELETE FROM books WHERE book_id=" + str(book_id))
    cursor.execute(query)
    connection.commit()
    return

if __name__=='__main__':
    connection = get_sql_connection()