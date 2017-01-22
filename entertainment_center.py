# Allow this file to use the media.py file
import media
import fresh_tomatoes

# Add movies to the website
toy_story = media.Movie("Toy Story", "Toys with a story!", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc", "PG")
avatar =  media.Movie("Avatar", "A Marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ", "PG-13")
matrix = media.Movie("Matrix", "A hacker takes the red pill", "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", "https://www.youtube.com/watch?v=m8e-FF8MsqU","R")
oceans_11 = media.Movie("Oceans Eleven", "Pretty people steal money", "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg", "https://www.youtube.com/watch?v=u7VTkceSsEw","E")

# Add TV Shows to the website
arrested_development = media.TVshow("Arrested Development", "The story of a wealthy family who lost everything and the one son who had no choice but to keep them all together", "https://upload.wikimedia.org/wikipedia/commons/e/e3/Arrested_Development.svg", "https://www.youtube.com/watch?v=TntmMY7N8ag","Netflix")
breaking_bad = media.TVshow("Breaking Bad", "A high school chemistry teach decides to cook meth", "https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png" ,"https://www.youtube.com/watch?v=HhesaQXLuRY", "AMC")
mad_men = media.TVshow("Mad Men", "An ad man from the 60s drinks a lot","https://upload.wikimedia.org/wikipedia/en/3/33/Mad-men-title-card.jpg","https://www.youtube.com/watch?v=m7NChV93LBw","AMC")


movies = [toy_story, avatar, matrix, oceans_11]
tv_shows = [arrested_development, breaking_bad, mad_men]

fresh_tomatoes.open_media_page(movies,tv_shows)