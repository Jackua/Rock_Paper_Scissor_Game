import random

def choiceAgainst():
    against = random.randint(1,3)
    if against == 1:
        return "Rock"
    elif against == 2:
        return "Paper"
    elif against == 3:
        return "Scissor"

def game(choice, choiceAgainst):
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
    points +=game(input("Rock, Paper, or Scissor: "), choiceAgainst())
    print("points: " + str(points))
    answer = input("Want to go again? Y or N: ")
    if answer == "Y":
        pass
    elif answer == "N":
        break