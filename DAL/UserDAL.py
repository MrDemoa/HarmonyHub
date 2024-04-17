import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.ConnectDB import ConnectSQL
from DTO.UserDTO import UserDTO

class UserDAL():

    con = ConnectSQL.connect_mysql()

    def getAllData():
        global con
        cursor = con.cursor()
        cursor.execute("select * from user")
        records = cursor.fetchall()
        cursor.close()
        return records

    def insert(user_dto):
        global con
        con = ConnectSQL.connect_mysql()
        cursor = con.cursor()
        cursor.execute("insert into user values(%s, %s, %s, %s)", (user_dto.userID, user_dto.username, user_dto.email, user_dto.password))
        con.commit()
        cursor.close()

    #def delete():

    def update(user_dto):
        global con
        cursor = con.cursor()
        cursor.execute("update user set username = %s, email = %s, password = %s where userID = %s", (user_dto.username, user_dto.email, user_dto.password, user_dto.userID))
        con.commit
        cursor.close()