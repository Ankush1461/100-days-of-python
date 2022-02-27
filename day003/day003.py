#TREASURE ISLAND GAME

#ascii art 
print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''');

print("\nWelcome to TREASURE ISLAND\n")
print("Your mission is to find the treasure\n")
choice1=input('''You're at a crossroad, where do you want to go? Type "left" or "right".\n''').lower()



if choice1=='left':
    # continue in the Game
    choice2=input('''You've come across a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat. Type "swim" to swim across.\n''').lower()
    if choice2=='wait':
        #Game will continue
        choice3=input('''You've arrived at the island unharmed. There is a house with 3 doors. One red, one blue and one yellow. Which color do you choose?\n''').lower()
        if choice3=='red':
            print('''It's a room full of fire. Game over.\n''')
        elif choice3=='blue':
            print('''You entered a room full of beasts. Game over.''' )
        elif choice3=='yellow':
            print('''You've found the treasure! You win.''' )
        else:
            print('''You chose a door that doesn't exist. Game over.\n''')
    else:
        print("You got attacked by an angry trout. Game over.\n")
else:
    print("You fell into a hole. Game over.\n")
