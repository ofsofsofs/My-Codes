import random


def odd_even():
    for i in range(100):
        a = random.randint(1, 9999999999999999)
        if (a % 2) == 0:
            print("the number is even")
        else:
            print("thw number is odd")


odd_even()
