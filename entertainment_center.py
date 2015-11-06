# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

# Below are my favorite movies
the_matrix = media.Movie("The Matrix",
                         "A man wakes up to the fact he's living in a vitual world.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=Q8g9zL-JL8E")


interstellar = media.Movie("Interstellar",
                           "A crew is dipatched to investigate potentially inhabitable planets.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")


mad_max_fury_road = media.Movie("Mad Max: Fury Road",
                                "A group of survivors battle the tyrant of a wasteland.",
                                "https://upload.wikimedia.org/wikipedia/en/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg",
                                "https://www.youtube.com/watch?v=hEJnMQG9ev8")


the_lord_of_the_rings_the_fellowship_of_the_ring = media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                                                               "A group of adventurers is dispatched to destroy a magical ring.",
                                                               "https://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg",
                                                               "https://www.youtube.com/watch?v=Pki6jbSbXIY")


the_social_network = media.Movie("The Social Network",
                                 "Mark Zuckerberg codes facebook but is later sued by his ex-partners.",
                                 "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                                 "https://www.youtube.com/watch?v=2RB3edZyeYw")

alien = media.Movie("Alien",
                    "A terrifying creature stalks a crew of miners in space.",
                    "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
                    "https://www.youtube.com/watch?v=bEVY_lonKf4")

# A list of movie objects
movies = [mad_max_fury_road, the_matrix, interstellar, alien,
          the_lord_of_the_rings_the_fellowship_of_the_ring, the_social_network]

# Opens the movie website
fresh_tomatoes.open_movies_page(movies)
