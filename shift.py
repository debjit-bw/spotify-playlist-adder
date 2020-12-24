import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import time

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#results = sp.user_playlist_tracks(user = "31azlbcfrhvohnk4y2ia2rop4wo4", playlist_id= "6UbQrM4QDDlZSh9ee38mP1", limit="50")
#pprint.pprint(results['items'][0])
#print(len(results['items']))
#print("ID:")
#print(results['items'][0]['track']['id'])
#print(results['tracks']['items'][0]['id'])
#print(sp.search(q="ben king stand by me", limit=1)['tracks']['items'][0]['id'])
#print(helo)
trackIdList = []

#https://open.spotify.com/user/8kp842smf0csa0pugkdzmyrc8
#https://open.spotify.com/playlist/5jqjfeGglbB05O9xnUql0D

from_pl = "5jqjfeGglbB05O9xnUql0D"
to_pl = "0GdlZXjwnLiEoDIB4FB5gL"
u_from = "i41olcpdly632zuk68nj0vdrz"
u_to = "xxkg9epsr8ev0c4css7mb6swh"

i =  0
while True:
    ids = ["spotify:track:" + item['track']['id'] for item in sp.user_playlist_tracks(user = u_from, playlist_id= from_pl, limit="50", offset=i)['items']]
    sp.user_playlist_add_tracks(user = u_to, playlist_id = to_pl, tracks = ids)
    i += len(ids)
    #print(i)
    #print(ids)
    if len(ids) < 50:
        break


#with open("logs.txt", mode = 'w', encoding="utf8") as logg:
#    for line in open("cleaned.txt", encoding="utf8"):
#        line = line.rstrip('\n')
#        try:
#            #print("searching" + line)
#            trackIdList.append(sp.search(q=line, limit=1)['tracks']['items'][0]['id'])
#            sp.user_playlist_add_tracks(user = "31azlbcfrhvohnk4y2ia2rop4wo4", playlist_id="6KpOvoBmcrYm0AalzpRThe", tracks=["spotify:track:" + trackIdList[-1]])
#            #print("done till here")
#            #print(helo)
#        except:
#            print("!!!!!!!!!!!! !!!!!! !!!" + line)
#            logg.write(line + '\n')
#            #raise
#        time.sleep(0.5)
#
##print(results)
##for id in trackIdList:
    