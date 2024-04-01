from shazamio import Shazam, Serialize
# Business Logic Layer
class BusinessLogic:
    @staticmethod
    def ping():
        return "Pong"
    @staticmethod
    def load_songs(self):
        song_ids = self.data_access.get_top_track()
        for song_id in song_ids:
            song = self.data_access.get_song(song_id)
            self.song_listbox.insert('end', song)
    
    @staticmethod
    def search_song_by_name(self):
        song_name = self.search_entry.get()
        song = self.data_access.get_song(song_name)
        self.song_listbox.insert('end', song)
        
    @staticmethod
    def search_song_by_artist(self):
        artist_name = self.search_entry.get()
        song = self.data_access.get_song_by_artist(artist_name)
        self.song_listbox.insert('end', song)
        
    @staticmethod
    def search_song_by_album(self):
        album_name = self.search_entry.get()
        song = self.data_access.get_song_by_album(album_name)
        self.song_listbox.insert('end', song)
        
    @staticmethod
    def search_song_by_genre(self):
        genre_name = self.search_entry.get()
        song = self.data_access.get_top_song_genre(genre_name)
        self.song_listbox.insert('end', song)
        
    @staticmethod
    def search_song_by_country(self):
        country_name = self.search_entry.get()
        song = self.data_access.get_top_song_country(country_name)
        self.song_listbox.insert('end', song)
       
    @staticmethod
    def search_song_by_id(self):
        song_id = self.search_entry.get()
        song = self.data_access.get_song_by_id(song_id)
        self.song_listbox.insert('end', song)
        
    @staticmethod
    def play_song(self):
        song_id = self.search_entry.get()
        song = self.data_access.get_song_by_id(song_id)
        self.data_access.play_song(song)
        
    @staticmethod
    def stop_song(self):
        self.data_access.stop_song()
        
    @staticmethod
    def pause_song(self):
        self.data_access.pause_song()
        
    @staticmethod
    def resume_song(self):
        self.data_access.resume_song()
        
    @staticmethod
    def next_song(self):
        self.data_access.next_song()
        
    @staticmethod
    def previous_song(self):
        self.data_access.previous_song()
        
    @staticmethod
    def shuffle_songs(self):
        self.data_access.shuffle_songs()
        
    @staticmethod
    def repeat_songs(self):
        self.data_access.repeat_songs()
        
    @staticmethod
    def show_song_info(self):
        song_id = self.search_entry.get()
        song = self.data_access.get_song_by_id(song_id)
        self.data_access.show_song_info(song)
        