import socket

def display_breaker():
  print("\n" + "#########"*3 + "\n")

def display_menu():
  return input("l:List | c:Change Track | k:kill Session | a:Add Session \n")

def display_Track_list():
  print("               Track              ")
  print("|--------------------------------|")
  print("| 1~ [event] champ-gregorien     |")
  print("| 2~ [event] corridor-discussion |")
  print("| 3~ [event] lecture-text        |")
  print("| 4~ [loop]  classe-gym          |")
  print("| 5~ [loop]  classe-musique      |")
  print("| 6~ [loop]  corridor            |")
  print("| 7~ [loop]  grillon             |")
  print("| 8~ [loop]  riviere             |")
  print("|--------------------------------|\n")
