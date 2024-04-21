import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)

from DAL.AlbumDAL import AlbumDAL

class AlbumBLL:
    def getAllData(self):
        return AlbumDAL.getAllData(self)

    def insert(album_dto):
        AlbumDAL.insert(album_dto)

    def delete(id):
        AlbumDAL.delete(id)

    def update(album_dto):
        AlbumDAL.update(album_dto)
