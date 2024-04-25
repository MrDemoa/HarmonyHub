import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from DAL.ConnectDB import ConnectSQL
from DTO.AlbumDTO import AlbumDTO

class AlbumDAL:

    con = ConnectSQL.connect_mysql()

    def getAllData(self):
        global con
        cursor = AlbumDAL.con.cursor()
        cursor.execute("select * from album")
        records = cursor.fetchall()
        cursor.close()
        return records

    def insert(album_dto):
        global con
        con = ConnectSQL.connect_mysql()
        cursor = con.cursor()
        cursor.execute("insert into album values(%s, %s, %s, %s, %s)", (album_dto.albumID, album_dto.title, album_dto.artistID, album_dto.genre, album_dto.releasedate))
        con.commit()
        cursor.close()

#Chua xong ham sua
    # def delete(self,id): 
    #     cursor = self.con.cursor()
    #     cursor.execute("delete from album where albumID = %s", (id,))
    #     count = int(cursor.rowcount)
    #     self.con.commit()
    #     cursor.close()

    #     if count > 0:
    #         print("Xoa thanh cong")
    #     else:
    #         print("ma khong ton tai")

    def update(self,album_dto):
        cursor = self.con.cursor()
        cursor.execute("update album set title = %s, artistID = %s, genre = %s, realeasedate = %s where albumID = %s", (album_dto.title, album_dto.artistID, album_dto.genre, album_dto.releasedate,album_dto.albumID))
        self.con.commit()
        cursor.close()