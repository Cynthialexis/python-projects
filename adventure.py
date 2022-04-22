name = input("Type your name: ")
print("Welcome,", name, "to this adventure.")

answer = input(
    "You're in the jungle, you have to escape and you can take the left path or the right path, which do you choose?").lower()

if answer == "left":
    answer = input("You come across a monkey, do you want to tame it of leave it be?").lower()

    if answer == "tame it":
        print("monkey kills you end of game")
    elif answer == "leave it be":
        print("you keep moving forward and the mokey ends up killing you")
    else:
        print("Not a valid option, you lose.") 

elif answer == "right":     
    answer = input("You come across a boat, you can either cross the river over it or keep walking what do you choose?").lower()

    if answer == "cross the river":
        print("as you cross the water a group of alligators knock over your boat, game over.")
    elif answer == "keep walking":
        print("you keep moving forward and you reach a tourist group that lead you to safety, Lilly, you won!")
    else:
        print("Not a valid option, you lose.") 
else:
    print("Not a valid option, you lose.")