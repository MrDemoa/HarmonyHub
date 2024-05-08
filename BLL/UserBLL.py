import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.UserDAL import UserDAL

class UserBLL:
    def getAllData(self):
        return UserDAL.getAllData(self)

    def insert(self,user_dto):
        UserDAL.insert(self,user_dto)

    def generateUserID(self):
        return UserDAL.generateUserID(self)

    def checkUsernameAndPass(self, username, password):
        return UserDAL.checkUsernameAndPass(self, username, password)
    
    def checkUsername(self, username):
        return UserDAL.checkUsername(self, username)
    
    def getUserIDByUsername(self, username):
        return UserDAL.checkUsernameAndPass(self, username)

    def update(self, user_dto):
        UserDAL.update(self,user_dto)

    def resetPassWord(self, username, password):
        UserDAL.resetPassWord(self, username, password)

