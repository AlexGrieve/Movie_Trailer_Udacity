import webbrowser

# Parent class to the Movie and TV Class, stores basic media information


class Media():

    def __init__(self, title, storyline, poster_image, trailer_youtube):
        # Initializes an instance of the Media class
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Uses webbrowser to open a media instance's trailer
        webbrowser.open(self.trailer_youtube_url)


# The Movie Class, child of the Media Class
class Movie(Media):
    """This class provides a way to store movie specific information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image, trailer_youtube, rating):
        # Initializes an instance of the movie class
        Media.__init__(self, title, storyline, poster_image, trailer_youtube)

        # Set the rating variable, but only if it is a valid rating
        if rating in Movie.VALID_RATINGS:
            self.rating = rating
        else:
            self.rating = "NA"

# The TVShow Class, child of the Media Class
class TVshow(Media):
    """This class provides a way to store TV specific information"""

    def __init__(self, title, storyline, poster_image, trailer_youtube, network):
        # Initializes an instance of the TVshow class
        Media.__init__(self, title, storyline, poster_image, trailer_youtube)
        self.network = network
