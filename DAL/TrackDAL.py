import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.ConnectDB import ConnectSQL
from DTO.TrackDTO import TrackDTO

class TrackDAL():

    con = ConnectSQL.connect_mysql()

    def getAllData(self):
        global con
        cursor = TrackDAL.con.cursor()
        cursor.execute("select * from track")
        records = cursor.fetchall()
        cursor.close()
        return records

    def generateTrackID(self):
        cursor = self.con.cursor()
        cursor.execute("select trackID from track order by trackID desc limit 1")
        track_id = cursor.fetchone()
        if track_id:
            id = track_id[0]
            id = int(id[1:]) + 1
        else:
            id = 1
        return "T" + str(id)


    def insert(self, track_dto):
        try:
            cursor = self.con.cursor()
            if track_dto.albumID == "None":
                track_dto.albumID = None
            cursor.execute("insert into track values(%s, %s, %s, %s, %s, %s)", (track_dto.trackID, track_dto.title, track_dto.artistID, track_dto.albumID, track_dto.duration, track_dto.releasedate))
            self.con.commit()
            cursor.close()
        except Exception as e:
            print("DAL TRACK:", str(e))

    def delete(self,trackID):
        cursor = self.con.cursor()
        cursor.execute("delete from track where trackID = %s", (trackID,))
        count = int(cursor.rowcount)
        self.con.commit()
        cursor.close()

        if count > 0:
            print("Xoa thanh cong")
        else:
            print("ma khong ton tai")

    def update(self,track_dto):
        cursor = self.con.cursor()
        if track_dto.albumID == "None":
                track_dto.albumID = None
        cursor.execute("update track set title = %s, artistID = %s, albumID = %s, duration = %s, realeasedate = %s where trackID = %s", ( track_dto.title, track_dto.artistID, track_dto.albumID, track_dto.duration, track_dto.releasedate, track_dto.trackID))
        self.con.commit()
        cursor.close()

# trackdal = TrackDAL()
#trackdal.generateTrackID()