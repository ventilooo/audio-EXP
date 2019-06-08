import vlc
import time
import random

OPTIONS = "sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=ogg,dst=:8080}"

instance = vlc.Instance()

#Create a MediaPlayer with the default instance
player = instance.media_player_new()

def set_track(player,media):
  player.set_media(media)
  player.play()


#Load the media file
forest = instance.media_new('./data/forest.mp3', OPTIONS)
god = instance.media_new('./data/god.mp3', OPTIONS)
kids = instance.media_new('./data/kids.mp3', OPTIONS)
water = instance.media_new('./data/water_wheel.mp3', OPTIONS)

set_track(player,forest)

while True:
  track = input("Select an audio track: 1:kids, 2:god, 3:water, 4:forest\n")
  if track == '1':
    set_track(player,kids)
  elif track == '2':
    set_track(player,god)
  elif track == '3':
    set_track(player,water)
  elif track == '4':
    set_track(player,forest)
  else:
    print('Wrong input\n')