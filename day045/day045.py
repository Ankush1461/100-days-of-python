# 100 Movies to Watch (Web Scraping) Program.

import requests
from bs4 import BeautifulSoup

URL = "https://stacker.com/stories/1587/100-best-movies-all-time/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all('h2', class_="ct-slideshow__slide__text-container__caption")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
