import random


def rock_paper_scissors():
    contiune_ = "y"
    list = ["rock", "paper", "scissors"]
    while contiune_ == "y":
        computer = random.choice(list)
        person = str(input("pls enter your choice: "))
        if (computer == "rock") and (person == "paper"):
            print(computer, person, "you win!")
        elif (computer == "paper") and (person == "scissors"):
            print(computer, person, "you win!")
        elif (computer == "scissors") and (person == "rock"):
            print(computer, person, "you win!")
        elif computer == person:
            print("Draw")
        else:
            print(computer, person, "you lost!")
        contiune_ = input("do you want to play again? ")


rock_paper_scissors()