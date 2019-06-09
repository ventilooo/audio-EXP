import socket

def ask_session():
  nb = input("Enter The number of Session : ")
  display_breaker()
  return int(nb)


def ask_media_with_session_id():
  nb = input("Session ID|media : \n")
  return nb.split('|')

def display_session(session):
  print(f"ID: {session.id}")
  print(f"Port: {session.port}\n")

def display_breaker():
  print("\n" + "#########"*3 + "\n")

def display_Track_list():
  print("## Track ##")
  print("|---------|")
  print("|  Tree   |")
  print("|  god    |")
  print("|  kid    |")
  print("|  water  |")
  print("|---------|\n")