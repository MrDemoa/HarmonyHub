import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.AlbumDAL import AlbumDAL

class AlbumBLL:
    def getAllData(self):
        return AlbumDAL.getAllData(self)

    def insert(album_dto):
        AlbumDAL.insert(album_dto)

    # def delete(self,id):
    #     AlbumDAL.delete(self,id)

    def update(self,album_dto):
        AlbumDAL.update(self,album_dto)
