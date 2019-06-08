import vlc
import time
import random

OPTIONS = "sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=ogg,dst=:8080}"

instance = vlc.Instance()

#Create a MediaPlayer with the default instance
player = instance.media_list_player_new()

#Load the media file

forest = instance.media_new('./data/forest.mp3', OPTIONS)
god = instance.media_new('./data/god.mp3', OPTIONS)
kids = instance.media_new('./data/kids.mp3', OPTIONS)
water = instance.media_new('./data/water_wheel.mp3', OPTIONS)

tracks = [forest, kids, water, god]
media_list = instance.media_list_new()

media_list.lock()
index = 0
for track in tracks:
  media_list.insert_media(track,index)
  index+=1
media_list.unlock()

player.set_media_list(media_list)
player.play()

while True:
  track = input("Press a key to play next track\n")
  if track != None:
    player.next()