import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.AlbumDAL import AlbumDAL

class AlbumBLL:
    def getAllData(self):
        return AlbumDAL.getAllData(self)

    def generateAlbumID(self):
        return AlbumDAL.generateAlbumID(self)

    def insert(self, album_dto):
        AlbumDAL.insert(self, album_dto)

    # def delete(self,id):
    #     AlbumDAL.delete(self,id)

    def update(self,album_dto):
        AlbumDAL.update(self,album_dto)
