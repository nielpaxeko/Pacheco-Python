import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# Get html from html and soupify it
response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

# Look for all movie titles, in this case all movie titles are h3 headings with the class of title
movies = soup.find_all("h3", class_="title")
# Append all of them to a list and reverse it
movie_list = [movie.getText() for movie in movies] # List comprehension
movie_list.reverse()

# Write to a new file
with open("topmovies.txt", "w") as file:
    for movie in movie_list:
        file.write(movie + "\n")
        