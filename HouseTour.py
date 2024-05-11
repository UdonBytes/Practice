import time

print("Welcome to the house!\n")
time.sleep(1)
print("Please use: 'Forward' and 'back' to control the tour.")
print("Only the naughty will use 'left' and 'right'.\n")
time.sleep(1)
print("You enter through the front door.\n")
time.sleep(1)

#Position:
#Outside = -1
#Closet = -2
#Entrance = 0
#Hallway 1 = 1
#Grand Piano = 2
#Dining Room = 3
#Kitchen = 4
#Family Room = 5

position = 0

user_input = str(input("Where would you like to go?\n").lower())

while True:
    if user_input == "forward":
        position = position + 1
        if position == 0:
            print("You are now in the entrance.")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == 1:
            print("You are now in the hallway. There is nothing much to see.")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == 2:
            print("You are now in the Grand Piano Room. Let's play a duet!")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == 3:
            print("You are now in the Dining Room. Food isn't ready yet.")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == 4:
            print("You are now in the Kitchen. Let's cook a meal together!")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == 5:
            print("You are now in the Family Room. There is a large sofa and a TV.")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == -1:
            print("\nYou have exited the house.")
            exit()
        else:
            print("\nYou have fallen into space.")
            exit()
    elif user_input == "back":
        position = position - 1
        if position == 0:
            print("You are now in the entrance.")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == 1:
            print("You are now in the hallway. There is nothing much to see.")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == 2:
            print("You are now in the Grand Piano Room. Let's play a duet!")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == 3:
            print("You are now in the Dining Room. Food isn't ready yet.")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == 4:
            print("You are now in the Kitchen. Let's cook a meal together!")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == 5:
            print("You are now in the Family Room. There is a large sofa and a TV.")
            user_input = str(input("\nWhere would you like to go?\n").lower())
        elif position == -1:
            print("\nYou have exited the house.")
            exit()
        else:
            print("\nYou have fallen into space.")
            exit()
    elif user_input == "left":
        print("You are now in the closet. It's dark in here.")
        time.sleep(1)
        closet_input = str(input("Would you like to come out of the closet? Yes/No\n").lower())
        if closet_input == "yes":
            print("Congratulations! Welcome to the LGBTQ community!")
            exit()
        elif closet_input == "no":
            print("Aww ok.")
            exit()           
        else:
            print(";)")
            exit()
    elif user_input == "right":
        print("You have walked into a wall and died.")
        exit()
    else:
        print("That is not a direction.")
        time.sleep(1)
        print("You have entered Hell.")
        exit()   
        
