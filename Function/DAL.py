import shazam

class DataAccessLayer:
    def __init__(self):
        self.shazam = shazam.Shazam()

    def get_song(self, song_id):
        return self.shazam.get_song(song_id)

    def get_artist(self, artist_id):
        return self.shazam.get_artist(artist_id)

    def get_album(self, album_id):
        return self.shazam.get_album(album_id)

    def get_playlist(self, playlist_id):
        return self.shazam.get_playlist(playlist_id)