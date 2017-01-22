# Movie_Trailer_Udacity

Repo contains the files to create an HTML page containing posters and trailers for Movies and TV Shows

--------
Running
--------
Creating the HTML output:
  - Clone the Repo
  - Run the entertainment_center.py file

Editing the content of the HTML output:
  - Add movies and TV shows to the entertainment_center.py file

---------- 
File List
----------
- entertainment_center.py: 
      - Python file where movie and tv data is provided to the class objects
      - Python file where methods are called to create the webpage
- media.py"
      - Python file containing three classes
          - Media: The partent class of TV and Movie, most data is stored here
          - Movie: Child of Media, contains movie specific data
          - TVShow: Child of Media, contains TV specific data
- fresh_tomatoes.py:
      - Python file that contains the style/formatting for the HTML output
      - Python file containing four methods:
          - create_movie_tiles_content: Iterates through provided movie data and formats it as output
          - create_tv_tiles_content: Iterates through provided TV data and formats it as output
          - open_media_page: Calls functions to create content, compiles and writes content to HTML output
          - extract_youtube_id: Extracts the YouTube ID from a URL
- fresh_movie_tomatoes.html:
      - HTML file containing the output for movie data
- fresh_tv_tomatoes.html: 
      - HTML file containing the output for TV show data
- fresh_tomatoes.pyc, media.pyc:
      - Compiled python code for the represented file
