import mysql.connector

class ConnectSQL():
    @staticmethod
    def connect_mysql():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='musicdb',
                user='root',
                password=''
            )
            if connection.is_connected():
                print("Connected to MySQL database")
                return connection
            else:
                print("Connection failed")
                return None
        except mysql.connector.Error as error:
            print("Error while connecting to MySQL", error)
            return None
