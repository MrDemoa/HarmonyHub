import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.UserDAL import UserDAL

class UserBLL:
    def getAllData(self):
        return UserDAL.getAllData(self)

    def hasUsername(self, username):
        return UserDAL.hasUsername(self, username)

    def insert(self,user_dto):
        UserDAL.insert(self,user_dto)

    def generateUserID(self):
        return UserDAL.generateUserID(self)

    def checkUsernameAndPass(self, username, password):
        return UserDAL.checkUsernameAndPass(self, username, password)
    
    def checkUsername(self, username):
        return UserDAL.checkUsername(self, username)
    
    def getUserIDByUsername(self, username):
        user_id= UserDAL.getUserIDByUsername(self, username)
        if user_id is None:
            print("User not found")
            return None
        else:
            return user_id
    def getUserNameByUserId(self, userID):
        username= UserDAL.getUserNameByUserID(self, userID)
        if username is None:
            print("User not found")
            return None
        else:
            return username
    def getUserInfoByUserID(self, userID):
        return UserDAL.getUserInfoByUserID(self, userID)
    def updateUserInfo(self, user_dto):
        UserDAL.updateUserInfo(self,user_dto)

    def resetPassWord(self, username, password):
        UserDAL.resetPassWord(self, username, password)

