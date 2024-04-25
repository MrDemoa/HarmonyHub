import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.UserDAL import UserDAL

class UserBLL:
    def getAllData(self):
        return UserDAL.getAllData(self)

    def insert(user_dto):
        UserDAL.insert(user_dto)

    def update(self,user_dto):
        UserDAL.update(self,user_dto)

