# checking the value of archer count system by using try-expect
try:
    archer_count = int(input("Please enter number of archers [8 - ∞]: "))  # taking archer count input
except ValueError:
    print("Invalid entry, please enter a integer this time!")
    archer_count = int(input("Number of archers [8 - ∞]: "))
else:
    while archer_count < 8:
        archer_count = int(input("Invalid entry, please enter again: "))

# creating empty list for using
rank = [0] * archer_count
name_surname = [0] * archer_count
points = [0] * archer_count
count_10 = [0] * archer_count
count_X = [0] * archer_count
sorted_points = []
final_sorted_points = []
sorted_names = [0] * archer_count
final_sorted_names = []
sorted_count_10 = []
final_sorted_count_10 = []
sorted_count_X = []
final_sorted_count_X = []


# creating a function that takes name and surnames
def take_name_surname():
    for i in range(archer_count):
        name_surname_input = input("Please enter the archer name and surname: ")
        name_surname[i] = name_surname_input


# creating a function that takes number of shots and points of each archer turn by turn
def shots():
    number_of_shots = int(input("Please enter the number of shots: "))  # taking the number of shots
    for x in range(number_of_shots):
        for y in range(archer_count):
            archer_point = int(input(f"Please enter the {y+1}. archer's {x+1}. shot [5-6-7-8-9-10-0]: "))
            while archer_point != 5 and archer_point != 6 and archer_point != 7 and archer_point != 8 and archer_point != 9 and archer_point != 10 and archer_point != 0:  # points need to be in[5,6,7,8,9,10,0]
                archer_point = int(input(f"Invalid entry, please enter the {y + 1}. archer's {x + 1}. shot [5-6-7-8-9-10-0]: "))
            points[y] += archer_point
            if archer_point == 10:
                ask_x = input("Is it a X shot[y/n]: ")
                if ask_x == "y":
                    count_10[y] += 1  # adding a one point to 10 point shot
                    count_X[y] += 1  # adding a one point to X point shot
                else:
                    count_10[y] += 1  # adding a one point to 10 point shot


def rank_points():
    # creating a loop to sort points and names
    for p in range(archer_count):
        highest_point = max(points)  # finding highest point in the list
        index = points.index(highest_point)  # creating new index for usage
        highest_10 = max(count_10)  # finding highest 10 count in the list
        highest_x = max(count_X)   # finding highest X count in the list
        if points.count(highest_point) > 1:  # checking for equality
            index = count_10.index(highest_10)
            if count_10.count(max(count_10)) > 1:  # checking for equality
                index = count_X.index(highest_x)

        sorted_count_10.append(count_10[index])  # finding new count 10
        count_10.pop(index)
        sorted_count_X.append(count_X[index])  # finding new count X
        count_X.pop(index)

        sorted_points.append(highest_point)  # finding new points
        points.remove(highest_point)

        sorted_names[p] = name_surname[index]  # finding new names
        name_surname.pop(index)


# function that creating rank from 1 to archer_count value
def ranker():
    for z in range(archer_count):
        rank[z] += z+1


# printing function to print needed info
def printer():
    print("Rank", "Name-Surname", "Points", "10 Count", "X Count")
    print("----", "------------", "------", "--------", "-------")
    for k in range(archer_count):
        print(f"{rank[k]:4d} {sorted_names[k]:>11} {sorted_points[k]:6d} {sorted_count_10[k]:8d} {sorted_count_X[k]:7d}")


# calling all needed functions
def main():
    take_name_surname()
    shots()
    ranker()
    rank_points()
    printer()


main()
