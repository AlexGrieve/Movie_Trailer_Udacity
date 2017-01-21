import webbrowser

# Parent class to the Movie and TV Class, stores basic media information
class Media():
	def __init__(self, title, description, poster_image, trailer_youtube):
		self.title = title
		self.storyline = description
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


# The Movie Class, child of the Media Class
class Movie(Media):
	"""This class provides a way to store movie specific information"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	# self is the instance of the class
	def __init__(self, title, storyline, poster_image, trailer_youtube):
		Media.__init__(self, title, storyline, poster_image, trailer_youtube)


# The Movie Class, child of the Media Class
class TVShow(Media):
	"""This class provides a way to store TV specific information"""
	def __init__(self, title, storyline, poster_image, trailer_youtube):
		Media.__init__(self, title, storyline, poster_image, trailer_youtube)


