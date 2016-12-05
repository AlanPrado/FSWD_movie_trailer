import webbrowser

class Movie():
    """This class provides a way to store movie related information
	
	Attributes:
		title = movie title
		story_line = a description for the movie
		poster_image_url = the image poster is location
		trailer_youtube_url = the movie trailer location
	
	Constants:
		VALID_RATINGS = used for rank movies
		
	"""
	
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_story_line, poster_image, trailer_youtube):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
	"""Open a dialog to show a trailer """
