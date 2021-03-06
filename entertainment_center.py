import fresh_tomatoes
import media

# Create movie instances and their parameters below.
fury = media.Movie("Fury",
                   "Tanks shooting stuff",
                   "http://img.moviepostershop.com/fury-movie-poster-2014-1020770902.jpg",  # noqa
                   "https://www.youtube.com/watch?v=DNHuK1rteF4")

alien = media.Movie("Alien",
                    "Aliens kill people",
                    "https://secure.i.telegraph.co.uk/multimedia/archive/03064/Alien-intro_3064438b.jpg",  # noqa
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")

castaway = media.Movie("Castaway",
                       "Guy on an island with Wilson",
                       "https://ia.media-imdb.com/images/M/MV5BN2Y5ZTU4YjctMDRmMC00MTg4LWE1M2MtMjk4MzVmOTE4YjkzXkEyXkFqcGdeQXVyNTc1NTQxODI@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
                       "https://www.youtube.com/watch?v=2TWYDogv4WQ")

jaws = media.Movie("Jaws",
                   "Shark go boom",
                   "https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/jaws-movie-poster-1975-the-titanic-project.jpg",  # noqa
                   "https://www.youtube.com/watch?v=U1fu_sA7XhE")

terminator = media.Movie("Terminator",
                         "I'll be back",
                         "https://stewartstaffordblog.files.wordpress.com/2015/01/the-terminator-poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=k64P4l2Wmeg")

tombstone = media.Movie("Tombstone",
                        "Western hit",
                        "http://www.ruthlessreviews.com/wp-content/uploads/2017/06/tombstone-meta.jpg",  # noqa
                        "https://www.youtube.com/watch?v=XTWYKf5hXIg")

# List of movie instances.
movies = [fury, alien, castaway, jaws, terminator, tombstone]

# Passes movie list and opens URL to movie page.
fresh_tomatoes.open_movies_page(movies)
