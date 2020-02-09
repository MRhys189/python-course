class Movie:
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # self is the object being created
        # rhs are variables we have to initialize
        # lhs of self in the brackets are the arguments
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def name(self):
        print(f"The name of the movie is {self.title}")


toy_story = Movie("Toy Story", "About a boy and his love for his toys",
                  "Image", "www.youtube.com/toy_story_trailer")

print(toy_story.name())
print(toy_story.title)
