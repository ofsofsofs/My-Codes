import random


def generating_number_of_2_and_sum():
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    print(f"{a} + {b} = ?")
    sum = a + b
    return sum


def controlling():
    contiune_ = "y"
    while contiune_ == "y":
        add = generating_number_of_2_and_sum()
        guess = int(input("pls enter your guess: "))
        while guess != add:
            print("wrong guess pls try again")
            guess = int(input("pls enter your guess: "))
        if guess == add:
            print("correct!")
        contiune_ = input("do you want to play again? ")


controlling()
