import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.TrackDAL import TrackDAL

class TrackBLL:
    def getAllData():
        TrackDAL.getAllData()

    def insert(track_dto):
        TrackDAL.insert(track_dto)

    def delete(Trackid):
        TrackDAL.delete(Trackid)

    def update(track_dto):
        TrackDAL.update(track_dto)