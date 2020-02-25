import random

def game(choice):
    choiceAgainst = random.choice(["Rock","Paper","Scissor"])
    if choice == "Rock" and choiceAgainst == "Paper":
        print("You Lose!")
        return -1
    elif choice == "Rock" and choiceAgainst == "Scissor":
        print("You Win!")
        return 1
    elif choice == "Paper" and choiceAgainst == "Scissor":
        print("You Lose!")
        return -1
    elif choice == "Paper" and choiceAgainst == "Rock":
        print("You Win!")
        return 1
    elif choice == "Scissor" and choiceAgainst == "Rock":
        print("You Lose!")
        return -1
    elif choice == "Scissor" and choiceAgainst == "Paper":
        print("You Win!")
        return 1
    elif choice == choiceAgainst:
        print("You Tied")
        return 0

points = 0

while True:
    points +=game(input("Rock, Paper, or Scissor: "))
    print("points: " + str(points))
    answer = input("Want to go again? Y or N: ")
    if answer == "Y":
        pass
    elif answer == "N":
        break