from native_lang import Native_lang

class Database:
    def __init__(self):
        self.native_languages = {}
        self._last_movie_key = 0

    def add_language(self, movie):
        self._last_movie_key += 1
        self.native_languages[self._last_movie_key] = movie
        return self._last_movie_key

    def delete_movie(self, movie_key):
        if movie_key in self.native_languages:
            del self.native_languages[movie_key]

    def get_movie(self, movie_key):
        movie = self.native_languages.get(movie_key)
        if movie is None:
            return None
        movie_ = Native_lang(movie.title, year=movie.year)
        return movie_

    def get_movies(self):
        movies = []
        for movie_key, movie in self.native_languages.items():
            movie_ = Native_lang(movie.title, year=movie.year)
            movies.append((movie_key, movie_))
        return movies