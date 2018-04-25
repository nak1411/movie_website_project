import webbrowser


class Movie():
    """ Contains movie related data such as title, story,
    poster image URL and trailer URL.

    Args:
        title (str): Title of movie instance.
        storyline (str): Description of storyline of movie instance.
        poster_image_url (str): URL to the movie's poster image.
        trailer_youtube_url (str): Youtube URL to the movie's trailer.

    Attributes:
        movie_title (str): Title of movie instance.
        movie_storyline (str): Description of storyline of movie instance.
        poster_image (str): URL to the movie's poster image.
        trailer_youtube (str): Youtube URL to the movie's trailer.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens browser to movie trailer URL."""
        webbrowser.open(self.trailer_youtube_url)
