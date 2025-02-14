from operator import indexOf
from time import strftime
import requests
import datetime as dt
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


# Load environment variables from the .env file
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_ID = os.getenv("SPOTIFY_USER_ID")
URL_REDIRECT = "http://example.com"


# Function to check if the input year format is correct
def checkFormat(input_year):
    try:
        dt.datetime.strptime(input_year, "%Y-%m-%d")
        print(f"{year} is formatted correctly")
        return True
    except ValueError:
        print(f"{year} is NOT formatted correctly")
        return False


def scrapeBillboard(year):
    URL = f"https://www.billboard.com/charts/hot-100/{year}"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }
    # Get html from html and soupify it
    response = requests.get(URL, headers=header)
    response.raise_for_status()
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")

    # Look for all song titles, in this case all song titles are h3 headings with the id of title-of-a-story
    songs = soup.select("li ul li h3#title-of-a-story")
    song_list = [song.get_text(strip=True) for song in songs]
    print("\nTop 100 Songs:")
    for song in song_list:
        print(f"{indexOf(song_list, song)+1}. {song}")
    return song_list

# Create spotify playlist using spotipy documentation 
def createPlaylist(song_list, year):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=URL_REDIRECT,
            scope="playlist-modify-public",
            username=USER_ID,
        )
    )
    
    # Create a new playlist
    playlist_name = f"Billboard Top 100 - {year}"
    playlist = sp.user_playlist_create(user=USER_ID, name=playlist_name, public=True)
    playlist_id = playlist["id"]
    print(f"Playlist '{playlist_name}' has been created!")
    
    track_uris = []
    for song in song_list:
        # Search for the songs on Spotify
        result = sp.search(q=song, limit=1, type="track")
        tracks = result.get("tracks", {}).get("items", [])
        if tracks:
            track_uri = tracks[0]["uri"]
            track_uris.append(track_uri)
            print(f"Added: {song}")
        else:
            print(f"Could not find the following song: {song}")

    # Add songs to the Spotify playlist
    if track_uris:
        sp.playlist_add_items(playlist_id, track_uris)
        print("All available songs added to the playlist!")
    
# Must type the following URL:
# https://example.com/?code=AQCC78Vrx0XXen3IlyT_8QYMHg7sWJ-Kz8-iqPa2sw0W3bePpNOw5GZpapYEBmuVXGLdt9k9RdeWtoY-xXmyGe9yl2g27_Jy_0FcgSYegszykwQ1OTNQFgkl2TmegCRMjdw4-Q1oRWqQ64DcR9SGdS5UX0BltVvHUh-CHzTa-zC56W94So_pELMcqIpjEg
year = input("What year would you like to travel to in YYYY-MM-DD format? ")
if checkFormat(year):
    songs = scrapeBillboard(year)
    createPlaylist(songs, year)
