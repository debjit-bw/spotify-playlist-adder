# spotify-playlist-adder

this code was written for our discord server "music junction" to preserve playlists


## raw.txt

contains groovy queues. for any other music provider, [clean.py](#)'s cleaning functions need to ne changed appropriately

preview:
> 101) Andrew Bird - Three White Horses       3:24 
> 102) The Beatles - Eight Days A Week        2:44 
> 103) Blackbird (Remastered 2009)            2:19 
> 104) Green Day - 21 Guns                    5:27 
> 105) One Direction - 18                     4:09 
> 106) 18 - EXES                              4:01 
> 107) Alessia Cara - Four Pink Walls         3:32 
> 108) Cold War Kids - First                  3:18 
> 109) Lukas Graham - 7 Years                 4:00 
> 110) Queen - Another One Bites the Dust     3:43 
> 111) When The End Comes - Official Studio…  5:55 


## clean .py

cleans data from raw.txt and puts them in cleaned.txt

preview:

> andrew bird three white horses 

> the beatles eight days a week

> blackbird

> green day 21 guns

> one direction 18

> 18 exes

> alessia cara four pink walls

> cold war kids first

> lukas graham 7 years

> queen another one bites the dust

> when the end comes studio



## final .py

creates the final playlist. you need to have the [proper environment variables available in your terminal](https://spotipy.readthedocs.io/en/2.6.3/#authorization-code-flow). you technically can edit some code to create a new playlist rhrough code, but i generally create a playlist at [spotify](https://open.spotify.com/).

it reads from cleaned .txt and searches spotify and adds the first search result into the playlist (playlist_id). beware avout permissions though. the scope "playlist-modify-private" can add only to pvt playlists. change the scope according to your needs.

songs that couldn't be added get added to logs .txt as well as printed onto the terminal.