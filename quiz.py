print("Welcome to the quiz game")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
score = 0    

answer = input("What is 10 + 10? ").lower()
if answer == "20":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What color does blue and yellow make? ").lower()
if answer == "green":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What animal makes an oink sound? ").lower()
if answer == "pig":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the main ingridient in guacamole? ").lower()
if answer == "avocado":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which Kardasian is dating Pete Davidson? ").lower()
if answer == "kim":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got ",str(score)," questions correct!")