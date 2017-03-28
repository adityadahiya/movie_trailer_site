import fresh_tomatoes
import media
#Instances of class movie in file media.py
logan = media.Movie("Logan",
                    "A mutant on his last journey to save a girl",
                    "logan.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

wonder_woman = media.Movie("Wonder Woman",
                           "A powerful princess comes to the man's"
                           " world frst time in order to end all wars",
                           "ww.jpg",
                           "https://www.youtube.com/watch?v=INLzqh7rZ-U")

bahubali_2 = media.Movie("Bahubali 2",
                         "Son takes his revenge on a tryant ruler"
                          "responsible for his father's death",
                         "b2.jpg",
                         "https://www.youtube.com/watch?v=G62HrubdD6o")

baywatch = media.Movie("Baywatch",
                       "Lifeguard Mitch Buchannon and a brash new recruit"
                       "uncover a criminal plot that threatens the future"
                       "of the bay.",
                       "bw.jpg",
                       "https://www.youtube.com/watch?v=nZ5tqzw841s")

fate_of_the_furious = media.Movie("The Fate of the Furious",
                                  "Last part of the fast and furious series",
                                  "ff.jpg",
                                  "https://www.youtube.com"
                                  "/watch?v=JwMKRevYa_M")

guardians_of_the_galaxy_2 = media.Movie("Guardians of the Galaxy 2",
                                        "A group of outcasts team up to"
                                        " save the galaxy",
                                        "download.jpg",
                                        "https://www.youtube.com"
                                        "/watch?v=2cv2ueYnKjg")

movies = [logan, wonder_woman, bahubali_2, baywatch,
         fate_of_the_furious, guardians_of_the_galaxy_2]
fresh_tomatoes.open_movies_page(movies)
  #the function open_movies_pages takes in a list of movies.
