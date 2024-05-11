import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.ConnectDB import ConnectSQL
from DTO.PLDetailDTO import PLDetailDTO

class PLDetailDAL:
    
    con = ConnectSQL.connect_mysql()

    def insertTracktoPlayList(self, pldetail_dto):
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM playlist_detail WHERE PlaylistID = %s AND trackID = %s", (pldetail_dto.PlaylistID, pldetail_dto.trackID))
        record = cursor.fetchone()
        if record:
            print("Record already exists")
        else:
            cursor.execute("insert into playlist_detail values(%s, %s, %s)", (pldetail_dto.PlaylistID, pldetail_dto.UserID, pldetail_dto.trackID))
            self.con.commit()
        cursor.close()

    def getTrackinPlayListofUserID(self, playlistID, userID):
        cursor = self.con.cursor()
        cursor.execute("SELECT track.trackID, track.title, track.artistID, track.albumID, track.duration, track.realeasedate FROM playlist_detail INNER JOIN `track` ON playlist_detail.trackID = track.trackID WHERE userID = %s  and playlistID = %s", (userID,playlistID))
        records = cursor.fetchall()
        self.con.commit()
        cursor.close()
        return records

    def deleteTrackInPlayList(self, trackID):
        cursor = self.con.cursor()
        cursor.execute("delete from detail_playlist where tracktrackID = %s", (trackID,))
        count = int(cursor.rowcount)
        self.con.commit()
        cursor.close()

        if count > 0:
            return True
        return False

pl = PLDetailDAL()
print(pl.getTrackinPlayListofUserID("PL0001", "0007"))