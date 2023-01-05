# constants
COLUMN_NUMBER = 11
MIN_ARCHER = 10

# checking the value of archer count system by using try-expect
try:
    archer_count = int(input("Please enter number of archers [10 - ∞]: "))  # taking archer count input
except ValueError:
    print("Invalid entry, please enter a integer this time!")
    archer_count = int(input("Number of archers [10 - ∞]: "))
else:
    while archer_count < MIN_ARCHER:
        archer_count = int(input("Invalid entry, please enter again: "))

number_of_shots = int(input("Please enter the number of shots: "))  # taking the number of shots
# defining wind types and wind dictionary
wind = {"North": 0, "Northeaster": 0, "Easterly": 0, "Southeaster": 0, "South": 0, "Southwester": 0, "Westerly": 0, "Northwester": 0}
wind_types = ["North", "Northeaster", "Easterly", "Southeaster", "South", "Southwester", "Westerly", "Northwester"]
# defining needed lists
missed_shots = [0]
archer_totals = [0] * archer_count
archers_and_points = {}
# defining needed lists
point_0 = [0] * archer_count
point_1 = [0] * archer_count
point_2 = [0] * archer_count
point_3 = [0] * archer_count
point_4 = [0] * archer_count
point_5 = [0] * archer_count
point_6 = [0] * archer_count
point_7 = [0] * archer_count
point_8 = [0] * archer_count
point_9 = [0] * archer_count
point_10 = [0] * archer_count
# defining needed lists
point_0_avg = [0]
point_1_avg = [0]
point_2_avg = [0]
point_3_avg = [0]
point_4_avg = [0]
point_5_avg = [0]
point_6_avg = [0]
point_7_avg = [0]
point_8_avg = [0]
point_9_avg = [0]
point_10_avg = [0]
# defining total shots have been shotted
total_shot = archer_count * number_of_shots
# defining needed lists
avg_wind = []


# creating function to create dictionary for archers and archers' points
def creating_dic():
    for i in range(1, archer_count+1):
        archers_and_points[i] = []


# creating function to get points from user
def shots_and_points():
    for x in range(number_of_shots):
        for y in range(archer_count):
            archer_point = int(input(f"Please enter the {y+1}. archer's {x+1}. shot [0 to 10]: "))
            archer_totals[y] += archer_point
            while archer_point > 10 or archer_point < 0:  # points needed to be in [0 to 10]
                archer_point = int(input(f"Invalid entry, please enter the {y + 1}. archer's {x + 1}. shot [0 to 10]: "))
            if archer_point == 0:
                wind_type = input(f"Please enter the wind type[North, Northeaster, Easterly, Southeaster, South, Southwester, Westerly, Northwester]: ")  # wind type from user
                missed_shots[0] += 1  # adding one to missed shot list
                if wind_type in wind:
                    wind[wind_type] += 1
            archers_and_points[y+1].append(archer_point)
    # calculating average for wind and wind types
    for i in range(8):
        if missed_shots[0] != 0:
            avg_wind.append(wind[wind_types[i]] / missed_shots[0] * 100)
        else:
            avg_wind.append(0)


# defining a function to place every point to right archer's place
def placing_points():
    for i in range(archer_count):
        for j in range(number_of_shots):
            if archers_and_points[i+1][j] == 0:
                point_0[i] += 1
            elif archers_and_points[i+1][j] == 1:
                point_1[i] += 1
            elif archers_and_points[i+1][j] == 2:
                point_2[i] += 1
            elif archers_and_points[i+1][j] == 3:
                point_3[i] += 1
            elif archers_and_points[i+1][j] == 4:
                point_4[i] += 1
            elif archers_and_points[i+1][j] == 5:
                point_5[i] += 1
            elif archers_and_points[i+1][j] == 6:
                point_6[i] += 1
            elif archers_and_points[i+1][j] == 7:
                point_7[i] += 1
            elif archers_and_points[i+1][j] == 8:
                point_8[i] += 1
            elif archers_and_points[i+1][j] == 9:
                point_9[i] += 1
            elif archers_and_points[i+1][j] == 10:
                point_10[i] += 1


# printing part that prints all needed information
def printings():
    print("Archer Reg No",  " 10 P ",  " 9 P  ",  " 8 P  ",  " 7 P  ",  " 6 P  ",  " 5 P  ",  " 4 P  ", " 3 P  ",  " 2 P  ",  " 1 P  ",  " O P  ",  " Total Points")
    print("-------------",  " -----",  " -----",  " -----",  " -----",  " -----",  " -----",  " -----", " -----",  " -----",  " -----",  " -----",  " ------------")
    for j in range(archer_count):
        print(f"{j+1:<14} {point_10[j]:<6} {point_9[j]:<6} {point_8[j]:<6} {point_7[j]:<6} {point_6[j]:<6} {point_5[j]:<6} {point_4[j]:<6} {point_3[j]:<6} {point_2[j]:<6} {point_1[j]:<6} {point_0[j]:<6} {archer_totals[j]:<13}")
        point_10_avg.append(point_10[j])
        point_9_avg.append(point_9[j])
        point_8_avg.append(point_8[j])
        point_7_avg.append(point_7[j])
        point_6_avg.append(point_6[j])
        point_5_avg.append(point_5[j])
        point_4_avg.append(point_4[j])
        point_3_avg.append(point_3[j])
        point_2_avg.append(point_2[j])
        point_1_avg.append(point_1[j])
        point_0_avg.append(point_0[j])
    print(f"All Archers(%) {sum(point_10_avg)/total_shot*100:<6.2f} {sum(point_9_avg)/total_shot*100:<6.2f} {sum(point_8_avg)/total_shot*100:<6.2f} {sum(point_7_avg)/total_shot*100:<6.2f} {sum(point_6_avg)/total_shot*100:<6.2f} {sum(point_5_avg)/total_shot*100:<6.2f} {sum(point_4_avg)/total_shot*100:<6.2f} {sum(point_3_avg)/total_shot*100:<6.2f} {sum(point_2_avg)/total_shot*100:<6.2f} {sum(point_1_avg)/total_shot*100:<6.2f} {sum(point_0_avg)/total_shot*100:<6.2f}")
    print("")
    print("Wind Name   ", "Missed Shot Rate (%)")
    print("----------- ", "--------------------")
    for i in range(8):
        print(f"{wind_types[i]:<12} {avg_wind[i]:<21.2f} ")


# creating a main function
def main():
    creating_dic()
    shots_and_points()
    placing_points()
    printings()


main()
