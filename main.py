print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input("So which way you want to go. Left or Right ?\n").lower()
if choice1 == "left":
  choice2 = input("Do you want to swim across the river or wait?\n ").lower()
  if choice2 == "wait":
    choice3 = input("Which door you choose to go through. Red, Yellow or Blue ?\n").lower()
    if choice3 == "yellow":
      print("You won!!! CONGRATULATIONS!!! yeahhhhhh!")
    elif choice3 == "red":
      print("You are burned by FIRE!!! GAME OVER!!!")
    elif choice3 == "blue":
      print("You are eaten by BEASTS!!! GAME OVER!!!") 
    else:
      print("GAME OVER!!!")
  else:
    print("You are attacked by trout. GAME OVER!!!")
else:
  print("Fall into a hole, GAME OVER!!!")

#printing the string with single quotes embedding the words in double quotes as a user choice to check for.
#print('You\'hv won this "game" "over" match')