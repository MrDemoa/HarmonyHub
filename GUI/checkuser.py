import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DTO.UserDTO import UserDTO
from BLL.UserBLL import UserBLL

class User_GUI:
    def insert():
        userid = input("Nhập user id: ")
        username = input("Nhập username: ")
        email = input("Nhập email: ")
        password = input("Nhập password: ")
        user_dto = UserDTO(userid, username, email, password)
        UserBLL.insert(user_dto)


User_GUI.insert()
