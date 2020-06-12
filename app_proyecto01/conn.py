import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='guota',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

        mySql_insert_query = """INSERT INTO prueba (pnombre, papellido, sapellido) 
                            VALUES 
                            ('Lenovo', 'ThinKpad', 'Antes IBM') """

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()

        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
