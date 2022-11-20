def feet_to_inches(num):
    inches = num * 12
    return inches


a = int(input("pls enter the number that you wanted to convert to inch: "))
inches = feet_to_inches(a)
print(inches)
