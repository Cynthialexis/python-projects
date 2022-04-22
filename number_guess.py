import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("type in a number greater then 0 next time")
        quit()

else: 
    print ("type in a number next time")
    quit()

r = random.randrange (top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print ("Please make another guess.")
        continue
    if user_guess == r:
        print("You got it!")
        break
    elif user_guess > r:
            print("You were above the number.")
    else:
            print("you were below the number")

print("you got it in", guesses, "guesses")