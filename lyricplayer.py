from api import SongFetcher

#take inputs from user and fetch the lyrics
song=input('Enter the song name : ')
artist=input('Enter the artist name : ')
album=input('Enter the album name : ')
songHandle=SongFetcher(song,artist,album)
songId=songHandle.getSongID()
if songId:
    songLyrics=songHandle.getSongLyrics(songId)
    print(songLyrics)









