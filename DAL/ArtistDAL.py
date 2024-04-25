import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from DAL.ConnectDB import ConnectSQL
from DTO.ArtistDTO import ArtistDTO

class ArtistDAL:

    con = ConnectSQL.connect_mysql()

    def getAllData(self):
        global con
        cursor = ArtistDAL.con.cursor()
        cursor.execute("select * from artist")
        records = cursor.fetchall()
        cursor.close()
        return records

    def generateArtistID(self):
        cursor = self.con.cursor()
        cursor.execute("select artistID from artist order by artistID desc limit 1")
        artist_id = cursor.fetchone()
        if artist_id :
            id = artist_id[0]
            id = int(id[2:]) + 1
        else:
            id = 1
        return "AT" + str(id)

    def insert(self,artist_dto):
        cursor = self.con.cursor()
        cursor.execute("insert into artist values(%s, %s, %s)", (artist_dto.artistID, artist_dto.name, artist_dto.genre))
        self.con.commit()
        cursor.close()

    def update(self,artist_dto):
        cursor = self.con.cursor()
        cursor.execute("update artist set name = %s, genre = %s where artistID = %s", (artist_dto.name, artist_dto.genre, artist_dto.artistID))
        self.con.commit()
        cursor.close()