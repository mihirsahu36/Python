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

choice1 = input('You\'re at a cross road. Where do you want to go? "left" or "right"\n').lower()

if choice1 == 'left':
  choice2 = input('You come to a lake. There is an island in middle of the lake. Type "wait" for wait for a boat or Type "swim" to swim across.\n').lower()
  if choice2 == 'wait':
    choice3 = input('You arrive at the island unharmed. There is a house with three doors. One red, one yellow, one blue. Which colour do you choose?\n').lower()
    if choice3 == 'blue':
      print("You came across a tiger who is hungry. Game Over!!!")
    elif choice3 == 'red':
      print("Behind the door there was cliff and you fell down. Game Over!!!")
    else:
      print("You found the treasure. Hooray You win!!!")
  else:
    print("You come across crocodile. Game Over!!!")
else:
  print("You fell in a hole. Game Over!!!")
 
