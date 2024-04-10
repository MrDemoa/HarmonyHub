import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.AlbumDAL import AlbumDAL

class AlbumBLL:
    def getAllData():
        AlbumDAL.getAllData()

    def insert(album_dto):
        AlbumDAL.insert(album_dto)

    def delete(id):
        AlbumDAL.delete(id)

    def update(Album_dto):
        AlbumDAL.update(album_dto)
