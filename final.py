import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import time

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

trackIdList = []

playlist_id = "###"
user_id = "###"

with open("logs.txt", mode = 'w', encoding="utf8") as logg:
    for line in open("cleaned.txt", encoding="utf8"):
        line = line.rstrip('\n')
        try:
            #print("searching" + line)
            trackIdList.append(sp.search(q=line, limit=1)['tracks']['items'][0]['id'])
            sp.user_playlist_add_tracks(user = user_id, playlist_id=playlist_id, tracks=["spotify:track:" + trackIdList[-1]])
            #print("done till here")
        except:
            print("!-----!\t" + line)
            logg.write(line + '\n')
            #raise
        time.sleep(0.1)

#print(results)
#for id in trackIdList:
    