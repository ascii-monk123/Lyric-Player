import json
import urllib.request as request
import urllib.error as err
import urllib.parse as ul
from config import reqApiData

##Song fetcher class
class SongFetcher:
    def __init__(self,songName:str,artist:str,album:str) -> None:
        self.songName=songName
        self.artist=artist
        self.album=album
    ####### this method handles all the logic behind fetching the song details from the server   
    @classmethod
    def fetchFromUrl(cls,path,type,**urlParams):
        url=ul.urlencode(urlParams)
        try:
            with request.urlopen("{}{}?{}".format(reqApiData.get('trackUrl'),path,url)) as f:
                urldata=f.read().decode("utf-8")
            urldata=json.loads(urldata)
            if type == 'songId':
                if(urldata['message']['body']['track_list']):
                    songId=urldata['message']['body']['track_list'][0]['track']['track_id']
                    return songId
            elif type=='lyrics':
                if(urldata['message']['body']['lyrics']['lyrics_body']):
                    return urldata['message']['body']['lyrics']['lyrics_body']
                else:
                    print('Sorry the data couldnt be found')
        except (err.URLError,KeyError,ValueError) as error:
            print("Error happened {}".format(error))
        return False
    #### this method is mainly responsible for fetching the song id 
    def getSongID(self)->str or bool:
        songDetails=self.fetchFromUrl('/track.search','songId',**{'q_artist':self.artist,'page_size':1,'page':1,'s_track_rating':'desc','format':'json','q_track':self.songName,'apikey':reqApiData.get('key')})
        return songDetails

    ### this method is mainly responsible for fetching the song lyrics from the server
    def getSongLyrics(self,songId:str)->str or bool:
        songLyrics=self.fetchFromUrl('track.lyrics.get','lyrics',**{'track_id':songId,'apikey':reqApiData.get('key')})
        return songLyrics
        
   

