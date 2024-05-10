import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.ConnectDB import ConnectSQL
from DTO.PLDetailDTO import PLDetailDTO

class PLDetailDAL:
    
    con = ConnectSQL.connect_mysql()

    def insertTracktoPlayList(self, pldetail_dto):
        cursor = self.con.cursor()
        cursor.execute("insert into playlist_detail values(%s, %s, %s)", (pldetail_dto.PlaylistID, pldetail_dto.UserID, pldetail_dto.trackID))
        self.con.commit()
        cursor.close()

    def deleteTrackInPlayList(self, trackID):
        cursor = self.con.cursor()
        cursor.execute("delete from detail_playlist where tracktrackID = %s", (trackID,))
        count = int(cursor.rowcount)
        self.con.commit()
        cursor.close()

        if count > 0:
            return True
        return False

