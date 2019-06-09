from session_vlc import Session, Instance
from ui import *

def create_sessions(nb_session):
  sessions = []
  vlc = Instance()
  while nb_session > 0:
    sessions.append(Session(vlc.instance))
    nb_session = nb_session - 1
  return sessions

def change_track(session, track_id):
  session.set_track(track_id)

def play_all(sessions):
  for session in sessions:
    session.set_track(session.tree())
    session.play()

if __name__ == '__main__':
  session_nb = ask_session()
  sessions = create_sessions(session_nb)

  play_all(sessions)

  for session in sessions:
    display_session(session)

  display_breaker()
  display_Track_list()

  while True:
    user = ask_media_with_session_id()
    user_id = int(user[0])
    track = int(user[1])
    for session in sessions:
      if session.id == user_id:
        session.choose_track(track)
        print(f"Session with ID: {session.id} on track {track}\n")

    display_breaker()
    display_Track_list()
