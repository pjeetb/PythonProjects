import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
#Defining the user input variable.
user_choice=int(input("What do you choose 0 for Rock, 1 for Paper & 2 for Scissor ?\n"))
print("You choose: ")
if user_choice >= 3 or user_choice < 0:
  print("Invalid Choice for the input.")
else:
    print(game_images[user_choice])
    #defining the computer variable.
    comp_choice = random.randint(0, 2)
    print("Computer choose: ")
    print(game_images[comp_choice])
    if user_choice == 0 and comp_choice == 2:
     print("You win!!!")
    elif comp_choice == 0 and user_choice == 2:
     print("You lose!!!")
    elif comp_choice > user_choice:
     print("you lose!!!")
    elif user_choice > comp_choice:
     print("You win!!!")
    elif comp_choice == user_choice:
     print("Its a draw!!!")
