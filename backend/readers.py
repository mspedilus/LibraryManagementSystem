from sql_connection import get_sql_connection

#Retrieves all readers in readers table
def getAllReaders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM readers")
    cursor.execute(query)
    response = []

    for (reader_id, first_name, last_name, email, phone_number, address, city, state, zip_code, country) in cursor:
        response.append({
                'first_name': first_name, 
                'last_name': last_name, 
                'email': email,
                'phone_number': phone_number, 
                'address': address,
                'city': city,
                'state': state,
                "zip_code": zip_code,
                'country': country,
                "reader_id": reader_id
        })
    return response


#Inserts a new reader into readers table
def insertNewReader(connection, reader):
    cursor = connection.cursor()
    query = ("INSERT INTO readers (reader_id, first_name, last_name, email, phone_number, address, city, state, zip_code, country) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    data = (reader['reader_id'], reader['first_name'], reader['last_name'], reader['email'],
            reader['phone_number'], reader['address'], reader['city'], reader['state'],
            reader['zip_code'], reader['country'])

    cursor.execute(query, data)
    connection.commit()
    return


#Deletes a reader from readers table
def deleteReader(connection, reader_id):
    cursor = connection.cursor()
    query = ("DELETE FROM readers WHERE reader_id=" + str(reader_id))
    cursor.execute(query)
    connection.commit()
    return

if __name__=='__main__':
    connection = get_sql_connection()
    # print(getAllReaders(connection))
    # print(insertNewReader(connection, {
    #    "reader_id": 41, "first_name": "Frank", "last_name": "While", "email": "fsd@gfsd.com", "phone_number":"123123123", 
    #    "address":"wer", "city":"wer", "state":"wre", "zip_code":"541", "country":""
    #  }))
    # print(deleteReader(connection, 41))