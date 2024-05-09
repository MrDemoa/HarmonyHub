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

    def generateUserID(self):
        cursor = self.con.cursor()
        cursor.execute("select userID from user order by userID desc limit 1")
        user_id = cursor.fetchone()
        if user_id :
            id = int(user_id[0]) + 1
        else:
            id = str(1)
        return str(id)

    def insert(self,user_dto):
        cursor = self.con.cursor()
        cursor.execute("insert into user values(%s, %s, %s, %s)", (str(user_dto.userID), str(user_dto.username), str(user_dto.email), str(user_dto.password)))
        self.con.commit()
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

    def getUserIDByUsername(self, username):
        if self.con is None:
            print("Connection is not established")
            return None

        cursor = self.con.cursor()

        if cursor is None:
            print("Failed to create cursor")
            return None

        cursor.execute("select userID from user where username = %s", (username,))
        user_id = cursor.fetchone()
        cursor.close()
        if user_id:
            return user_id[0]
        else:
            return None
        
    def getUserNameByUserID(self, userID):
        cursor = self.con.cursor()
        cursor.execute("select username from user where userID = %s", (userID,))
        username = cursor.fetchone()
        cursor.close()
        return username[0]
       

    def update(self, user_dto):
        cursor = self.con.cursor()
        cursor.execute("update user set username = %s, email = %s, password = %s where userID = %s", (user_dto.username, user_dto.email, user_dto.password, user_dto.userID))
        self.con.commit()
        cursor.close()

    def checkUsername(self, username):
        cursor = self.con.cursor()
        cursor.execute("select * from user where username = %s", (username,))
        records = cursor.fetchall()
        self.con.commit()
        cursor.close()
        if records:
            return True
        else:
            return False

    def resetPassWord(self, username, password):
        cursor = self.con.cursor()
        cursor.execute("update user set password = %s where username = %s", (password, username))
        self.con.commit()
        cursor.close()

# userdal = UserDAL()
# print(userdal.getUserNameByUserID(3))