import webbrowser


class Movie():
    """ This class contains movie related data such as ratings, title, story,
    poster image and trailer URL."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Inits Movie class with title, story, poster image and trailer URL
        strings."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens Youtube URL and plays movie trailer."""
        webbrowser.open(self.trailer_youtube_url)
