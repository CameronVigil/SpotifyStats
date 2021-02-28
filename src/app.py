from flask import Flask, jsonify
from flask_cors import CORS
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import top as t
from Naked.toolshed.shell import execute_js, muterun_js
import sys


#variables
os.environ['SPOTIPY_CLIENT_ID'] = '70501fc412a34877a1becc7cf260d1f7'
os.environ['SPOTIPY_CLIENT_SECRET'] = '1a881808393e46fa8e146e460e0ab56e'
sid = os.getenv('SPOTIPY_CLIENT_ID')
ssecret = os.environ.get('SPOTIPY_CLIENT_SECRET')
spotify_client_username = '1217890391'
spotify_client_redirect_uri = 'http://localhost:8888/callback/'
scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,redirect_uri=spotify_client_redirect_uri))
#
# configuration
DEBUG = True

# # instantiate the app
# app = Flask(__name__)
# app.config.from_object(__name__)

# # enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})


# # sanity check route
# @app.route('/', methods=['GET'])
# def ping_pong():
#     main()
#     return

def main():
    playlists = sp.current_user_playlists(limit=50)
    top_album_set = []
    top_albums = []
    
    top_track_set = []
    top_tracks = []

    t.get_top_artists(sp)
    t.get_top_tracks(sp,top_track_set,top_tracks)
    t.get_top_albums(sp,top_album_set,top_albums)
    

if __name__ == '__main__':
    #app.run()
    main()