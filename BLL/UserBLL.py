import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.UserDAL import UserDAL

class UserBLL:
    def getAllData():
        UserDAL.getAllData()

    def insert(user_dto):
        UserDAL.insert(user_dto)

    def update(user_dto):
        UserDAL.update(user_dto)

