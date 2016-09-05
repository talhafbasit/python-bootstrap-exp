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

# build up the movie array
movie0 = media.Movie(d["movies"][0]["title"],
                         d["movies"][0]["storyline"],
                         d["movies"][0]["poster"],
                         d["movies"][0]["trailer"]
                         )
movie1 = media.Movie(d["movies"][1]["title"],
                         d["movies"][1]["storyline"],
                         d["movies"][1]["poster"],
                         d["movies"][1]["trailer"]
                         )
movie2 = media.Movie(d["movies"][2]["title"],
                         d["movies"][2]["storyline"],
                         d["movies"][2]["poster"],
                         d["movies"][2]["trailer"]
                         )
movie3 = media.Movie(d["movies"][3]["title"],
                         d["movies"][3]["storyline"],
                         d["movies"][3]["poster"],
                         d["movies"][3]["trailer"]
                         )

movies = [movie0, movie1, movie2, movie3]

# the simple bootstrap wrapper that we are using to generate the web page
fresh_tomatoes.open_movies_page(movies)
