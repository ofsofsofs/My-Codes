def max_finder():
    a = int(input("pls enter first number: "))
    b = int(input("psl enter other number: "))
    if a > b:
        max_number = a
        return max_number
    else:
        max_number = b
        return max_number


max_no = max_finder()
print(max_no)
