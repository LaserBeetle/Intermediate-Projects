import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SONGS_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_URL = "https://api.spotify.com/v1/"
CLIENT_ID = "25425c27942441c8919ab26525634362"
CLIENT_SECRET = "73bdcaaefa4242d482ebc40574f4146a"
REDIRECT_URI = "http://example.com"

date = input("Which date do you want to travel to? Type it in this format: YYYY-MM-DD:\n")

response = requests.get(url=SONGS_URL + date)
data = response.text

soup = BeautifulSoup(data, "html.parser")
titles = [title.getText().strip() for title in soup.find_all(name="h3", class_="c-title")]
titles_formatted = titles[6:-16:4]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        show_dialog=True
    )
)
user_id = sp.current_user()["id"]

song_uri = []

for song in titles:
    result = sp.search(q=f"track:{titles} year: {date.split('-')[0]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["name"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesnt exist in Spotify. Skipped.")

print(titles_formatted)
print(song_uri)