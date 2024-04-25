import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.ConnectDB import ConnectSQL
from DTO.UserDTO import UserDTO

class UserDAL():

    con = ConnectSQL.connect_mysql()

    def getAllData(self):
        global con
        cursor = UserDAL.con.cursor()
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

    def checkUsernameAndPass(self, username, password):
        cursor = self.con.cursor()
        cursor.execute("select * from user where username = %s and password = %s", (username, password))
        records = cursor.fetchall()
        self.con.commit()
        cursor.close()
        if records:
            return True
        else:
            return False

    def update(self,user_dto):
        cursor = self.con.cursor()
        cursor.execute("update user set username = %s, email = %s, password = %s where userID = %s", (user_dto.username, user_dto.email, user_dto.password, user_dto.userID))
        self.con.commit()
        cursor.close()

userdal = UserDAL()
