import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import top as t
from Naked.toolshed.shell import execute_js, muterun_js

#variables
os.environ['SPOTIPY_CLIENT_ID'] = '70501fc412a34877a1becc7cf260d1f7' #my personal spotify api info from spotify web app
os.environ['SPOTIPY_CLIENT_SECRET'] = '1a881808393e46fa8e146e460e0ab56e'
sid = os.getenv('SPOTIPY_CLIENT_ID')
ssecret = os.environ.get('SPOTIPY_CLIENT_SECRET')
spotify_client_username = '1217890391'
spotify_client_redirect_uri = 'http://localhost:8888/callback/'
scope = 'user-top-read'

# configuration
DEBUG = True

def main():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,redirect_uri=spotify_client_redirect_uri))

    playlists = sp.current_user_playlists(limit=50)
    
    #gets artist, track, album data from spotify API, runs functions in top.py
    t.get_top_artists(sp)
    t.get_top_tracks(sp)
    t.get_top_albums(sp)

if __name__ == '__main__':
    main()