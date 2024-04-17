import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.ArtistDAL import ArtistDAL

class ArtistBLL:
    def getAllData():
        ArtistDAL.getAllData()

    def insert(artist_dto):
        ArtistDAL.insert(artist_dto)

    def update(artist_dto):
        ArtistDAL.update(artist_dto)