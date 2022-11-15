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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You're alone, and you have no tools to help you find the treasure.\n Now you need to decide which direction you want to go")
direction1 = input("you choose to go... ")
if ("right") in direction1.lower():
    print("After couple of minutes walking, you spot a bear.\n")
    print("Now you have couple of options, you can fight the bear, you can sneak around the bear, or you can turn back and choose different direction")
    directionbear = input("You choose to...")
    if ("back") in directionbear.lower():
        print("Right just before you start to walk, the bear spotted you.\n Wasted!")
    else :
        print("The bear spotted you.\n Wasted!")
if ("left") in direction1.lower():
    print("You found a river, you can only go across by swimming or you can go across by waiting for a miracle to happen")
    directionriver = input("You choose to...")
    if ("wait") in directionriver.lower():
        print("Suddenly a lightning bolt fall through the sky, hit the river and all the water in the river is suddenly gone")
        print("Then you see 3 doors on the ground.\n There are red, yellow, and blue door")
        directiondoor = input("You open the")
        if directiondoor.lower() == "yellow":
            print("You win!")
        elif directiondoor.lower() == "red":
            print("There is a treasure box inside, you open the treasure box, then suddenly you're surrounded by some strange fire.\n Burned by fire.\n Wasted!")
        elif directiondoor.lower() == "blue":
            print("On the other side of the door, it's a jungle, you choose to walk through the door then the door is suddenly closed.")
            print("You heard, some strange sound, it kept getting closer, then suddenly you can't feel your own body.\n Head severed by a beast.\n Wasted!")
        else:
            print("You wake up in heaven")
    elif ("swim") in directionriver.lower():
        print("You're getting attacked by piranha swarms.\n Wasted!")
    else:
        print("God didn't like what you choose, and for some reason God decided to throw lightning bolt towards your direction.\n Wasted! ")