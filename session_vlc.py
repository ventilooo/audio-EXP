import vlc
import random

class Session:

  OPTIONS = "sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=ogg,dst=:8080}"

  def __init__(self, instance, id):
    self.instance = instance
    self.id = id
    self.player = self.instance.media_player_new()
    self.port = str(random.randint(8000,9000))
    self.options = self.OPTIONS.replace('8080', self.port)

  def kill(self):
   self.player.realease()

  def state(self):
    if self.player.is_playing():
      return "STOP"
    else:
      return "PLAYING"

  # media access method

  def tree(self):
    return self.instance.media_new('./data/forest.mp3', self.options)

  def church(self):
    return self.instance.media_new('./data/god.mp3', self.options)

  def kid(self):
    return self.instance.media_new('./data/kids.mp3', self.options)

  def water(self):
    return self.instance.media_new('./data/water_wheel.mp3', self.options)


  def play(self):
    self.player.play()

  def set_track(self, media):
    self.player.set_media(media)
    self.player.play()

  def choose_track(self,track):
    if track == 1:
      self.set_track(self.tree())
    elif track == 2:
      self.set_track(self.church())
    elif track == 3:
      self.set_track(self.kid())
    elif track == 4:
      self.set_track(self.water())


  def __str__(self):
    return f"session({self.port})"

  def __repr__(self):
    return f"session({self.port})"

class Instance:

  def __init__(self):
    self.instance = vlc.Instance()
