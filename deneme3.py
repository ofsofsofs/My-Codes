def factoriel(num):
    if num == 0:
        return 1
    else:
        return num * factoriel(num - 1)


number = int(input("pls enter your number: "))
print(factoriel(number))
