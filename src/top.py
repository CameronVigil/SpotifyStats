import json

#######gets top artists########
def get_top_artists(sp):
    ranges = ['short_term', 'medium_term', 'long_term']
    results = []
    
    # overall, last 6 months , last month
    for sp_range in ranges: 
        result = sp.current_user_top_artists(time_range=sp_range, limit=12)
        results.append(result['items'])

    #writes JSON data to respective JSON files for each time length
    with open('public/artist_short.json', 'w',encoding='utf-8') as f:
        json.dump(results[0], f, ensure_ascii=False,indent=4)
    with open('public/artist_medium.json', 'w',encoding='utf-8') as f:
        json.dump(results[1], f, ensure_ascii=False,indent=4)
    with open('public/artist_long.json', 'w',encoding='utf-8') as f:
        json.dump(results[2], f, ensure_ascii=False,indent=4)

########gets top tracks#######
def get_top_tracks(sp):
    ranges = ['short_term', 'medium_term', 'long_term']
    results = []

    #writes JSON data to respective json files
    for sp_range in ranges:# overall, last 6 months , last month
        result = sp.current_user_top_tracks(time_range=sp_range, limit=6)
        results.append(result['items'])
    with open('public/track_short.json', 'w',encoding='utf-8') as f:
            json.dump(results[0], f, ensure_ascii=False,indent=4)
    with open('public/track_medium.json', 'w',encoding='utf-8') as f:
            json.dump(results[1], f, ensure_ascii=False,indent=4)
    with open('public/track_long.json', 'w',encoding='utf-8') as f:
            json.dump(results[2], f, ensure_ascii=False,indent=4)


#######gets top albums########
def get_top_albums(sp):
    #based on song data, since Spotify API does not have a way to get album data
    ranges = ['short_term', 'medium_term', 'long_term']
    results = []
    
    for sp_range in ranges:
        find = False
        result = sp.current_user_top_tracks(time_range=sp_range, limit=3)
        results.append(result['items'])

    #writes JSON data to album.json
    with open('public/album_short.json', 'w',encoding='utf-8') as f:
            json.dump(results[0], f, ensure_ascii=False,indent=4)
    with open('public/album_medium.json', 'w',encoding='utf-8') as f:
            json.dump(results[1], f, ensure_ascii=False,indent=4)
    with open('public/album_long.json', 'w',encoding='utf-8') as f:
            json.dump(results[2], f, ensure_ascii=False,indent=4)

