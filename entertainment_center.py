import media
import fresh_tomatoes
from pprint import pprint
import json

# we read our movie data from json data file
# if this was production code we would check for errors, etc.
with open("movies.json") as json_data:
    d = json.load(json_data)
    json_data.close()
    #pprint(d)


movies = []
for movie_data in d["movies"]:
    #create instance of Movie class for each json object
    movie = media.Movie(movie_data["title"],
                        movie_data["storyline"],
                        movie_data["poster"],
                        movie_data["trailer"])
    #add new movie to list
    movies.append(movie)


# the simple bootstrap wrapper that we are using to generate the web page
fresh_tomatoes.open_movies_page(movies)
