import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.ConnectDB import ConnectSQL
from DTO.PlayListDTO import PlayListDTO

class PlayListDAL:
    
    con = ConnectSQL.connect_mysql()

    def getAllData(self):
        global con
        cursor = PlayListDAL.con.cursor()
        cursor.execute("select * from playlist")
        records = cursor.fetchall()
        cursor.close()
        return records
    
    def getDataPlaylistFromUserID(self, userID):
        cursor = self.con.cursor()
        cursor.execute("select playlistID, title, creationdate from playlist where userID = %s", (userID))
        records = cursor.fetchall()
        cursor.close()
        return records

    def generatePlaylistID(self):
        cursor = self.con.cursor()
        cursor.execute("select PlaylistID from playlist order by playlistID desc limit 1")
        playlist_id = cursor.fetchone()
        if playlist_id:
            id = playlist_id[0]
            id = int(id[1:]) + 1
        else:
            id = 1
        return "PL" + str(id).zfill(4)

    def insert(self, playlist_dto):
        cursor = self.con.cursor()
        cursor.execute("insert into playlist values(%s, %s, %s, %s, %s)", (playlist_dto.playlistID, playlist_dto.userID, playlist_dto.title, playlist_dto.creationdate))
        self.con.commit()
        cursor.close()

    def delete(id):
        global con 
        cursor = con.cursor()
        cursor.execute("delete from playlist where playlistID = %s", (id,))
        count = int(cursor.rowcount)
        con.commit()
        cursor.close()

        if count > 0:
            print("Xoa thanh cong")
        else:
            print("ma khong ton tai")

    def update(playlist_dto):
        global con
        cursor = con.cursor()
        cursor.execute("update playlist set userID = %s, title = %s, creationdate = %s where playlistID = %s", (playlist_dto.userID, playlist_dto.title, playlist_dto.creationdate, playlist_dto.playlistID))
        con.commit
        cursor.close()
    