#------------------------------------------------------------------------------
# Created By: Evan Smart
# Created On: 03/10/2023
# Version: 2.0
# Class: CS 30
# Assignment: Map RPG
#------------------------------------------------------------------------------
"""
Runs a continuous rpg where you can move around a map and search for items
"""
#------------------------------------------------------------------------------
# Global variables for column and row
column = 0
row = 2
# Formats the map in rows and columns
Ship_map = [
  ["PirateTile", "NothingTile", "StorageTile", "EscapeTile"],
  ["NothingTile", "StorageTile", "DeckTile","WheelHouseTile"],
  ["StartTile", "PirateTile", "RoomTile", "StorageTile"],
  ["BoilerTile", "NothingTile", "PirateTile", "NothingTile"]
]
#Nested Dictionary for all inventory items
Objects = {"Gun":
          {"Description": "A weapon that does 45 damage"},
          "MedKit":
          {"Description": "A kit that can heal 30 health"},
          "Knife":
          {"Description": "A weapon that does 20 damage"},
          "Food":
          {"Description": "A meal that can heal 10 health"}
          }
Ship_keys = ("PirateTile", "NothingTile", "StorageTile", "EscapeTile", "DeckTile", "WheelHouseTile", "StartTile", "RoomTile", "BoilerTile")
Ship_tiles = {"PirateTile": 
              {"Description": "There are pirates in here"},
              "NothingTile": 
              {"Description":"You are in an empty room"},
              "StorageTile": 
              {"Description":"You are in a storage room",                   "Inventory": "[Food]"},
              "EscapeTile": 
              {"Description":"You've made it to the rafts"},
              "DeckTile": 
              {"Description":"You are on the Deck"},
              "WheelHouseTile":
              {"Description":"You are behind the wheel of the ship", "Inventory": "[Gun]"},
              "StartTile": 
              {"Description":"You are on the starting tile"},
              "RoomTile":
              {"Description":"You are in your room",                        "Inventory": "[MedKit]"},
              "BoilerTile": 
              {"Description":"You are in the boiler room",                  "Inventory": "[Knife]"}
             }
# Empty list that contains Inventory
Inventory = []
# Function for all movement
def Movement():
    """
    Allows user to move around
    """
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
# Function for Finding Items
def Look():
    """
    Allows user to look around the room
    """
    global row, column
    searching = True
    while searching:
        searching = False
        if current_location == "StorageTile":
            print("You've found some food")
            if "Food" not in Inventory:
                Inventory.append("Food")
            else:
                Food = (input("You've already got some food do you really need more? "))
                if Food.lower() == "yes":
                    Inventory.append("Food")
                elif Food.lower() == "no":
                    print("You leave the food behind")
                else:
                    print("That's not a valid response")
        elif current_location == "RoomTile":
            print("You've found a medkit")
            if "MedKit" not in Inventory:
                Inventory.append("MedKit")
            else:
                print("You already have a Medkit")
        elif current_location == "BoilerTile":
            print("You've found a knife")
            if "Knife" not in Inventory:
                Inventory.append("Knife")
            else:
                print("You only need one knife")
        elif current_location == "WheelHouseTile":
            print("You've found a gun")
            if "Gun" not in Inventory:
                Inventory.append("Gun")
            else:
                print("You already have a gun")
        else:
            print("There's nothing in here")
  
# Code to print players current location
while True:
    current_location = Ship_map[row][column]
    if current_location in Ship_keys:
        print(Ship_tiles[current_location]["Description"])
    else:
        print("Something went wrong!")
 #Code for Main Menu
    choice = input("What would you like to do: Walk, Search, Check Inventory, or Quit: ")
    if choice == "walk" or choice == "Walk":
        Movement()
    elif choice == "quit" or choice == "Quit":
        print("Thank you for playing")
        break
    elif choice == "search" or choice == "Search":
        Look()
    elif choice == "Check Inventory" or choice == "check inventory":
      print(Inventory)
    else:
        print("You can't do that")