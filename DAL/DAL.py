import asyncio
from shazamio import Shazam, Serialize

class DataAccess:
    def __init__(self):
        self.shazamio = Shazam()
    
    async def get_song_by_id(self, query):
        song = await self.shazamio.track_about(query)
        return song
    
    async def get_song(self, query):
        track = await self.shazamio.search_track(query=query)
        return track
    
    async def get_artist(self, query):
        artist = await self.shazamio.search_artist(query=query)
        return artist
    
    async def get_artist_info(self):
        artist_info = await self.shazamio.artist_about("artist_id")
        print(f"Artist name: {artist_info['name']}")
        print(f"Genre: {artist_info['genres'][0]}")
        print(f"Followers: {artist_info['followers']}")
        
    async def get_track_info(self):
        track_info = await self.shazamio.track_about("track_id")
        print(f"Title: {track_info['title']}")
        print(f"Artist: {track_info['subtitle']}")
        print(f"Genre: {track_info['genres'][0]}")
        print(f"Release date: {track_info['release_date']}")
          
    async def get_top_track(self):
        top_tracks = await self.shazamio.top_world_tracks()
        return top_tracks
        
    async def get_song_by_artist(self, query):
        artist = await self.shazamio.search_artist(query=query)
        songs = await self.shazamio.artist_top_tracks(artist['id'])
        return songs
    
    async def get_song_by_album(self, query):
        album = await self.shazamio.search_album(query=query)
        songs = await self.shazamio.album_tracks(album['id'])
        return songs
    
    async def get_top_song_country(self, query):
        songs = await self.shazamio.top_country_tracks(query=query)
        return songs
    
    async def get_top_song_genre(self, query):
        songs = await self.shazamio.top_world_genre_tracks(query=query)
        return songs
    
    async def related_tracks(self, query):
        track = await self.shazamio.search_track(query=query)
        related = await self.shazamio.related_tracks(track['id'])
        return related
    
    
    

    

    