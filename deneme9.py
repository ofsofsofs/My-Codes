def calc_average():
    avg = 0
    for i in range(5):
        a = int(input("pls enter your grade: "))
        avg += a / 5
        a = 0
    return avg


def determine_grade():
    average = calc_average()
    if average >= 90:
        print("your grade is A!")
    elif average>=80 and average <=89:
        print("your grade is B!")
    elif average >= 80 and average <= 89:
        print("your grade is C!")
    elif average >= 70 and average <= 79:
        print("your grade is D!")
    else:
        print("your grade is F!")


determine_grade()
