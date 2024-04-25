import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.ArtistDAL import ArtistDAL

class ArtistBLL:
    def getAllData(self):
        return ArtistDAL.getAllData(self)

    def generateArtistID(self):
        return ArtistDAL.generateArtistID(self)

    def insert(artist_dto):
        ArtistDAL.insert(artist_dto)

    def update(self,artist_dto):
        ArtistDAL.update(self,artist_dto)