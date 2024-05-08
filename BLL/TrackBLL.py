import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.TrackDAL import TrackDAL

class TrackBLL:
    def getAllData(self):
        return TrackDAL.getAllData(self)

    def generateTrackID(self):
        return TrackDAL.generateTrackID(self)

    def insert(self, track_dto):
        TrackDAL.insert(self, track_dto)

    def delete(self,Trackid):
        TrackDAL.delete(self,Trackid)

    def update(self,track_dto):
        TrackDAL.update(self,track_dto)