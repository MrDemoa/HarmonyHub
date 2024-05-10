import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.PlayListDAL import PlayListDAL

class PlayListBLL:

    def getAllData(self):
        return PlayListDAL.getAllData(self)
    
    def getDataPlaylistFromUserID(self, userID):
        return PlayListDAL.getDataPlaylistFromUserID(self, userID)

    def generatePlaylistID(self):
        return PlayListDAL.generatePlaylistID(self)

    def insert(self,playlist_dto):
        PlayListDAL.insert(self,playlist_dto)

    def delete(self,id):
        return PlayListDAL.delete(self,id)
        

    def update(playlist_dto):
        PlayListDAL.update(playlist_dto)

