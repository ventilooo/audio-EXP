import vlc
import random

class Session:

  OPTIONS = "sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=ogg,dst=:8080}"

  def __init__(self, instance, ref, port):
    self.instance = instance
    self.ref = ref
    self.player = self.instance.media_player_new()
    self.options = self.OPTIONS.replace('8080', port)
    self.port = port
    self.set_track(self.loop_grillon())
    self.active_track = "grillon_loop"

  def state(self):
    if self.active_track == 'dead':
      return "Unref"
    if self.player.is_playing():
      return "STOP"
    else:
      return "PLAYING"


  def chant_gregorien(self):
    return self.instance.media_new('./data/event_champ_gregorien.mp3', self.options)

  def corridor_discussion(self):
    return self.instance.media_new('./data/event_corridor_discussions.mp3', self.options)

  def lecture_text(self):
    return self.instance.media_new('./data/event_lecture_texte.mp3', self.options)

  def classe_gym(self):
    return self.instance.media_new('./data/loop_classe_gym.mp3', self.options)

  def classe_musique(self):
    return self.instance.media_new('./data/loop_classe_musique.mp3', self.options)

  def loop_corridor(self):
    return self.instance.media_new('./data/loop_corridor.mp3', self.options)

  def loop_grillon(self):
    return self.instance.media_new('./data/loop_grillons.mp3', self.options)

  def loop_riviere(self):
    return self.instance.media_new('./data/loop_riviere.mp3', self.options)

  def play(self):
    self.player.play()

  def set_track(self, media):
    self.player.set_media(media)
    self.player.play()

  def choose_track(self,track):
    if track == 1:
      self.set_track(self.chant_gregorien())
      self.active_track = "chant"
    elif track == 2:
      self.set_track(self.corridor_discussion())
      self.active_track = "corrirdor_dicussision"
    elif track == 3:
      self.set_track(self.lecture_text())
      self.active_track = "lecture_text"
    elif track == 4:
      self.set_track(self.classe_gym())
      self.active_track = "gym"
    elif track == 5:
      self.set_track(self.classe_musique())
      self.active_track = "musique"
    elif track == 6:
      self.set_track(self.loop_corridor())
      self.active_track = "corridor_loop"
    elif track == 7:
      self.set_track(self.loop_grillon())
      self.active_track = "grillon_loop"
    elif track == 8:
      self.set_track(self.loop_riviere())
      self.active_track = "river_loop"

  def __str__(self):
    return f"session({self.port})"

  def __repr__(self):
    return f"session({self.port})"

class Instance:

  def __init__(self):
    self.instance = vlc.Instance()
