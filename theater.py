from movie import Movie
class Theater:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.movies = []
    def add_movie(self, movie):
        self.movies.append(movie)
    def show_movies(self):
        print("Movies playing at", self.name)
        for idx, movie in enumerate(self.movies, start=1):
            print(f"{idx}. {movie.title}")
