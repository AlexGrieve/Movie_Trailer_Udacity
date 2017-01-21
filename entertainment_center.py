# Allow this file to use the media.py file
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "Toys with a story!", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar =  media.Movie("Avatar", "A Marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ")
matrix = media.Movie("Matrix", "A hacker takes the red pill", "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", "https://www.youtube.com/watch?v=m8e-FF8MsqU")
oceans_11 = media.Movie("Oceans Eleven", "Pretty people steal money", "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg", "https://www.youtube.com/watch?v=u7VTkceSsEw")

movies = [toy_story, avatar, matrix, oceans_11]

fresh_tomatoes.open_media_page(movies)