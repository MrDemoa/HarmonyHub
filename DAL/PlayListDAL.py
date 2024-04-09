import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.ConnectDB import ConnectSQL
from DTO.PlayListDTO import PlayListDTO

class PlayListDAL:

    con = ConnectSQL.connect_mysql()

    def getAllData():
        global con
        cursor = con.cursor()
        cursor.execute("select * from playlist")
        records = cursor.fetchall()
        cursor.close()
        return records

    def insert(playlist_dto):
        global con
        con = ConnectSQL.connect_mysql()
        cursor = con.cursor()
        cursor.execute("insert into playlist values(%s, %s, %s, %s)", (playlist_dto.playlistID, playlist_dto.userID, playlist_dto.title, playlist_dto.creationdate))
        con.commit()
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