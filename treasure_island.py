print(f"Welcome to treasure island \nYour mission is to find the treasure")
first_step = input("You are at a cross road. Where do you want to go? Left or Right? ").lower()
if first_step == "right" or first_step == " ":
    print("Fall into a Hole \n Game Over")
elif first_step == "left":
    second_step = input(
        "Now you come to a lake.\nThere is an island in the middle of the lake.\nType 'wait' to wait for a boat or type 'swim' to cross the lake ").lower()
    if second_step == "swim" or second_step == " ":
        print("Attacked by trout\n Game Over")
    elif second_step == "wait":
        third_step = input(
            "You have arrived in the island unharmed\nThere is a house with 3 doors\nOne Red, one yellow and one blue?\nWhich color do you choose?: ").lower()
        if third_step == "blue" or third_step == " ":
            print("Eaten by beasts \n Game Over")
        elif third_step == "red":
            print("Burned by fire \n Game Over")
        elif third_step == "yellow":
            print("You Won")
        else:
            print("Game Over")
    else:
        print("Attacked by Trout \n Game Over")
else:
    print("Fall into a hole \n Game Over")
# game finished
