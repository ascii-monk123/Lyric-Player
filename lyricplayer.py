import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from api import SongFetcher

class Player(GridLayout):
    def __init__(self,**keywargs):
        super(Player,self).__init__(**keywargs)
        #music array
        self.music=[]
        self.currentSongLine,self.nextSongLine="",""
        self.cols=1
        self.setDefaultWindow()

        #lyric ui   
    def pressed(self,instance):
        song=self.songName.text
        artist=self.artist.text
        album=self.album.text
        songHandle=SongFetcher(song,artist,album)
        songId=songHandle.getSongID()
        songLyrics=False
        if songId:
            songLyrics=songHandle.getSongLyrics(songId)
            if songLyrics:
                self.music=[line for line in songLyrics.split('\n') if len(line)>=1]
        elif not songId or songLyrics:
            self.music=['No songs found ','There might be an api error or incorrect song typed. Please try again']

        self.clearInputs()
        self.changeWindow()

    #clear the input fields
    def clearInputs(self):
        self.album.text,self.songName.text,self.artist.text='','',''
    
    #change window as soon as song loads
    def changeWindow(self):
        try:
            self.remove_widget(self.submit)
            self.remove_widget(self.inside)
        except:
            pass   
        self.inside=GridLayout()
        self.inside.cols=1
        self.topLyrics=Label(text=f"{self.music[0]}",font_size=20)
        self.bottomLyrics=Label(text=f"{self.music[1]}",font_size=12)
        self.add_widget(self.topLyrics)
        self.add_widget(self.bottomLyrics)
        self.add_widget(self.inside)
        self.closePlayer=Button(text="EXIT",font_size=24,size_hint =(.5, .28), 
    pos =(20, 20))
        self.closePlayer.bind(on_press=self.setDefaultWindow)
        self.add_widget(self.closePlayer)
        self.lyricLength=len(self.music)
        self.currentLength=1
        self.clock=Clock.schedule_interval(self.updateLyrics,3)

    #update the lyrics
    def updateLyrics(self,*args):
        self.topLyrics.text=f"{self.music[self.currentLength]}"
        if self.currentLength<self.lyricLength-1:
            self.bottomLyrics.text=f"{self.music[self.currentLength+1]}"   
        else:
            self.bottomLyrics.text='End'
            self.clock.cancel()
        self.currentLength+=1

    #set up the default window method
    def setDefaultWindow(self,*args):
        try:
            self.remove_widget(self.topLyrics)
            self.remove_widget(self.bottomLyrics)
            self.clock.cancel()
            self.remove_widget(self.closePlayer)
            self.remove_widget(self.inside)
        except :
            pass
        self.inside=GridLayout()
        self.inside.cols=2
        #take song name
        self.inside.add_widget(Label(text="Enter Song Name : ",font_size=20))
        self.songName=TextInput(multiline=False,font_size=30,halign='center',padding=[25])
        self.inside.add_widget(self.songName)

        #take artist name input
        self.inside.add_widget(Label(text="Enter artist name : ",font_size=20))
        self.artist=TextInput(multiline=False,font_size=30,halign='center',padding=[25])
        self.inside.add_widget(self.artist)

        #take album name input
        self.inside.add_widget(Label(text="Enter Album Name : ",font_size=20))
        self.album=TextInput(multiline=False,font_size=30,halign='center',padding=[25])
        self.inside.add_widget(self.album)

        #bind inner grid to the outer grid
        self.add_widget(self.inside)

        #the submit button
        self.submit=Button(text="Submit",font_size=24,size_hint =(.5, .25), 
    pos =(20, 20))
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)


class LyricPlayer(App):
    def build(self):
        return Player()

if __name__=='__main__':
    LyricPlayer().run()
#this shall run the script













