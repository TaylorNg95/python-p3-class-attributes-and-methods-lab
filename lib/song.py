class Song:
    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_genre_count(genre)
        Song.add_to_artists(artist)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in [key for key, value in cls.genre_count.items()]:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in [key for key, value in cls.artist_count.items()]:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1