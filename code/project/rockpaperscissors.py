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

#Write your code below this line 👇
import random
print("\nRock! Paper! Scissors!")
weapons = [rock, paper, scissors]
odd = random.randint(0, 2)
computer= weapons[odd]
player = input("What do you choose?\n")
print(f"Computer chooses\n {computer}")
if ("rock") in player.lower():
    print(f"\nYou choose\n {rock}")
    if computer == rock:
         print("Draw!")
    elif computer == paper:
        print("You lose!")
    else:
        print("You win!")
elif ("paper") in player.lower():
    print(f"\nYou choose\n {paper}")
    if computer == rock:
         print("You lose!")
    elif computer == paper:
        print("Draw!")
    else:
        print("You win!")
elif ("scissors") in player.lower():
    print(f"\nYou choose\n {scissors}")
    if computer == rock:
         print("You lose!")
    elif computer == paper:
        print("You win!")
    else:
        print("Draw!")
else:
    print("I have no idea what that is")
