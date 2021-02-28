import json

#######gets top artists########
def get_top_artists(sp):
    ranges = ['short_term', 'medium_term', 'long_term']
    top_artist_set = []
    top_artists = []
    for sp_range in ranges: # all-time, last 6 months , last month
        results = sp.current_user_top_artists(time_range=sp_range, limit=10)
        print(results['items'])
        for i, item in enumerate(results['items']):
            top_artist_set.append(str(item['name']))
            pass
        top_artists.append(json.dumps(top_artist_set))
        
        #print(top_artists)
        top_artist_set.clear()
    # for i in range(len(top_artists)):
    #     print(ranges[i])
    #     print(top_artists[i])
    #return(top_artists[2])
    
    #prints top artists by range
    sp_range_index = 0
    
    for i in top_artists:
        #print("\n" + ranges[sp_range_index])
        for artist in i:
            #print(artist)
            pass
        sp_range_index = sp_range_index + 1

        #print("\n\n\n")


########gets top tracks#######
def get_top_tracks(sp,top_track_set,top_tracks):
    ranges = ['short_term', 'medium_term', 'long_term']

    for sp_range in ranges:
        results = sp.current_user_top_tracks(time_range=sp_range, limit=10)

        for i, item in enumerate(results['items']):
            #print(item['name'], 'by', item['artists'][0]['name'])
            top_track_set.append([item['name'],item['artists'][0]['name']])

        top_tracks.append(top_track_set)
        #print(top_tracks)
        top_track_set.clear()

    #print("\n\n\n")


#######gets top albums########
def get_top_albums(sp, top_album_set, top_albums):
    #based on song data, since Spotify API does not have a way to get album data
    ranges = ['short_term', 'medium_term', 'long_term']
    
    for sp_range in ranges:
        find = False
        results = sp.current_user_top_tracks(time_range=sp_range, limit=50)

        for i, item in enumerate(results['items']):
            if len(top_album_set) == 10:
                find = True
                break    
            if item['album']['name'] not in top_album_set:
                top_album_set.append(str(item['album']['name']))
            #print(item['album']['name'], 'by', item['artists'][0]['name'])
        if find:
            top_albums.append(str(top_album_set))
            #print(top_album_set)
            top_album_set.clear()
            #print(top_albums)
            print("\n")
    
    #print("\n\n\n")
