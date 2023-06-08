
import ipdb

class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist 
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

 
        
    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
  


    @classmethod
    def add_to_artists(cls, art):
        if art not in cls.artists:
            cls.artists.append(art)

    @classmethod
    def add_to_genre_count(cls, genre):
        
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, art):
        if cls.artist_count.get(art):
            cls.artist_count[art] += 1
        else:
            cls.artist_count[art] = 1

    


