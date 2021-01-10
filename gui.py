import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from api import SongFetcher
import time
music='''Baby I'm preying on you tonight
Hunt you down eat you alive
Just like animals
Animals
Like animals

Maybe you think that you can hide
I can smell your scent for miles
Just like animals
Animals
Like animals
Baby I'm

So what you trying to do to me
It's like we can't stop we're enemies
But we get along when I'm inside you
You're like a drug that's killing me
I cut you out entirely
But I get so high when I'm inside you

Yeah you can start over you can run free
You can find other fish in the sea
You can pretend it's meant to be
But you can't stay away from me
I can still hear you making that sound
Taking me down rolling on the ground
You can pretend that it was me
But no

Baby I'm preying on you tonight
Hunt you down eat you alive
Just like animals
Animals
Like animals

Maybe you think that you can hide
I can smell your scent for miles
Just like animals
...

******* This Lyrics isnt for commercial purposes ******** '''
music=music.split('\r\n')
print(music)
class Player(GridLayout):
    def __init__(self,**keywargs):
        super(Player,self).__init__(**keywargs)
        #current songline
        self.currentSongLine,self.nextSongLine="",""
        self.cols=1
        self.setDefaultWindow()

        #lyric ui   
    def pressed(self,instance):
        song=self.songName.text
        artist=self.artist.text
        album=self.album.text
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
        self.closePlayer=Button(text="EXIT",font_size=24,size_hint =(.5, .28), 
    pos =(20, 20))
        self.closePlayer.bind(on_press=self.setDefaultWindow)
        self.add_widget(self.closePlayer)
        self.inside=GridLayout()
        self.inside.cols=1
        self.topLyrics=Label(text="",font_size=20)
        self.bottomLyrics=Label(text="",font_size=12)
        self.add_widget(self.inside)
        self.lyricLength=len(music)
        self.currentLength=0
        self.clock=Clock.schedule_interval(self.updateLyrics,1)
    def updateLyrics(self,*args):
        self.topLyrics.text=f"{music[self.currentLength]}"
        if self.currentLength<self.lyricLength-1:
            self.bottomLyrics.text=f"{music[self.currentLength+1]}"
            self.currentLength+=1
            self.inside.add_widget(self.topLyrics)
            self.inside.add_widget(self.bottomLyrics)
        else:
            self.bottomLyrics.text='End'
            self.inside.add_widget(self.topLyrics)
            self.inside.add_widget(self.bottomLyrics)
            self.clock.cancel()


        
        
       


    #set up the default window method
    def setDefaultWindow(self,*something):
        try:
            self.clock.cancel()
            self.remove_widget(self.closePlayer)
            self.remove_widget(self.inside)
        except :
            pass
        #next songline
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













