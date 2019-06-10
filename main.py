from session_vlc import Session, Instance
import vlc
from ui import *

VLC = vlc.Instance()
SESSIONS = []

def search_track(ref):
  for e in SESSIONS:
    if e.ref == ref:
      return e
  print("No session found for this ID, check available ID with (l)\n")

def create_action():
  data = input("Enter information : [id|port]").split('|')

  ref = data[0]
  port = data[1]

  session = Session(VLC, ref, port)
  SESSIONS.append(session)

  print(f"Session {session.ref} created\n")

def list_action():
  if SESSIONS:
    for e in SESSIONS:
      print(f"ID: {e.ref} | Active Track: {e.active_track} | Port: {e.port} | State: {e.state()} \n")
  else:
    print("No session available, you create one first\n")

def change_track_action():
  display_Track_list()
  data = input("Enter information: [id|track]\n").split('|')
  ref = data[0]
  track = int(data[1])
  s = search_track(ref)
  s.choose_track(track)
  print(f"\n {s} on track:{track}\n")

def kill_action():
  ref = input("Enter information : [id] \n")
  s = search_track(ref)
  s.active_track = "dead"
  s.player.stop()

def main():
  while True:
    action = display_menu()
    if action == 'l':
      list_action()
    elif action == 'c':
      change_track_action()
    elif action == 'k':
      kill_action()
    elif action == 'a':
      create_action()


if __name__ == '__main__':
  main()