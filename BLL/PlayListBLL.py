import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.PlayListDAL import PlayListDAL

class PlayListBLL:
    def getAllData():
        PlayListDAL.getAllData()

    def insert(playlist_dto):
        PlayListDAL.insert(playlist_dto)

    def delete(id):
        PlayListDAL.delete(id)

    def update(playlist_dto):
        PlayListDAL.update(playlist_dto)

