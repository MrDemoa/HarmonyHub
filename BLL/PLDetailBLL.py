import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.PLDetailDAL import PLDetailDAL

class PLDetailBLL:


    def insertTracktoPlayList(self, playlist_dto):
        PLDetailDAL.insertTracktoPlayList(self, playlist_dto)

    def getTrackinPlayListofUserID(self, playlistID, userID):
        return PLDetailDAL.getTrackinPlayListofUserID(self, playlistID, userID)

    def udeleteTrackInPlayList(self, trackID):
        PLDetailDAL.update(self, trackID)

