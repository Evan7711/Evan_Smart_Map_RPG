#------------------------------------------------------------------------------
# Created By: Evan Smart
# Created On: 03/10/2023
# Version: 1.0
# Class: CS 30
# Assignment: Map RPG
#------------------------------------------------------------------------------
# Global variables for column and row
column = 0
row = 2

# Formats the map in rows and columns
Ship_map = [
  ["PirateTile", "NothingTile", "StorageTile", "EscapeTile"],
  ["NothingTile", "StorageTile", "DeckTile", "WheelHouseTile"],
  ["StartTile", "PirateTile", "RoomTile", "StorageTile"],
  ["BoilerTile", "NothingTile", "PirateTile", "NothingTile"]
]


# contains all the code for movement
def Movement():
  global row, column
  while True:
    Direction = input("Would you like to travel North, South, East, West: ")
    if Direction == "north" or Direction == "North":
      if row > 0:
        row -= 1
        break
      else:
        print("you can't go that way")
    elif Direction == "south" or Direction == "South":
      if row < 3:
        row += 1
        break
      else:
        print("you can't go that way")
    elif Direction == "east" or Direction == "East":
      if column < 3:
        column += 1
        break
      else:
        print("you can't go that way")
    elif Direction == "west" or Direction == "West":
      if column > 0:
        column -= 1
        break
      else:
        print("you can't go that way")
    else:
      print("You can't do that")

# Code to print players current location
while True:
  current_location = Ship_map[row][column]
  if current_location == "StartTile":
    print(f"You are on the starting tile")
  elif current_location == "NothingTile":
    print("You are in an empty room")
  elif current_location == "PirateTile":
    print("There are pirates in here")
  elif current_location == "BoilerTile":
    print("You are in the boiler room")
  elif current_location == "RoomTile":
    print("You are in your room")
  elif current_location == "StorageTile":
    print("You are in a storage room")
  elif current_location =="EscapeTile":
    print("You've made it to the rafts")
  elif current_location == "WheelHouseTile":
    print("You are behind the wheel of the ship")
  elif current_location == "DeckTile":
    print("You are on the Deck")
  else:
    print("Something went wrong!")

  # Code for Main Menu
  choice = input("What would you like to do: Walk or Quit: ")
  if choice == "walk" or "Walk":
    Movement()
  elif choice == "quit" or "Quit":
    print("Thank you for playing")
    break
  else:
    print("You can't do that")