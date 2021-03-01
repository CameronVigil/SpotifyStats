import json

#######gets top artists########
def get_top_artists(sp):
    ranges = ['short_term', 'medium_term', 'long_term']
    top_artist_set = []
    top_artists = []
    for sp_range in ranges: # all-time, last 6 months , last month
        results = sp.current_user_top_artists(time_range=sp_range, limit=10)
        for i, item in enumerate(results['items']):
            top_artist_set.append(item['name'])
        top_artists.append(json.dumps(top_artist_set))        
        top_artist_set.clear()
    top_artists = json.dumps(top_artists)

    #writes JSON data to artist.json
    with open('artist.json', 'w',encoding='utf-8') as f:
        json.dump(top_artists, f, ensure_ascii=False,indent=4)
    
########gets top tracks#######
def get_top_tracks(sp):
    ranges = ['short_term', 'medium_term', 'long_term']
    top_track_set = []
    top_tracks = []
    for sp_range in ranges:
        results = sp.current_user_top_tracks(time_range=sp_range, limit=10)
        for i, item in enumerate(results['items']):
            top_track_set.append([item['name'],item['artists'][0]['name']])
        top_tracks.append(json.dumps(top_track_set))
        top_track_set.clear()
    top_tracks = json.dumps(top_tracks)
    
    #writes JSON data to track.json
    with open('track.json', 'w',encoding='utf-8') as f:
        json.dump(top_tracks, f, ensure_ascii=False,indent=4)

#######gets top albums########
def get_top_albums(sp):
    #based on song data, since Spotify API does not have a way to get album data
    ranges = ['short_term', 'medium_term', 'long_term']
    top_album_set = []
    top_albums = []
    for sp_range in ranges:
        find = False
        results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
        for i, item in enumerate(results['items']):
            if len(top_album_set) == 10:
                find = True
                break
            if item['album']['name'] not in top_album_set:
                top_album_set.append(item['album']['name'])
        if find:
            top_albums.append(json.dumps(top_album_set))
            top_album_set.clear()
    top_albums = json.dumps(top_albums)
    
    #writes JSON data to album.json
    with open('album.json', 'w',encoding='utf-8') as f:
        json.dump(top_albums, f, ensure_ascii=False,indent=4)
