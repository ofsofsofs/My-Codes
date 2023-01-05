PERCENTAGE_DIVIDER = 2  # constant

# defining all names for calculations and usage
accepted_taws = 0
returned_taws = 0

accepted_boxes = 0
returned_boxes = 0
all_boxes = 0

same_weight_boxes = 0
lighter_boxes = 0
heavier_boxes = 0

heaviest_weight_of_taw = 0
heaviest_number_of_taws = 0
largest_weight_of_taw = 0
largest_number_of_taws = 0

max_difference = 0
min_difference = 99999
total_difference_lighter = 0
total_difference_heavier = 0
heavy_taw_weight = 0
light_taw_weight = 0
total_taw_weight = 0

default_weight = 0
percentage_calculator_max = 0
percentage_calculator_min = 0

diff_counter = 0
continuous_num = 0
rep = 0
different_weight = 0
valid_box = True

max_sign = ""
min_sign = ""
box_continue = "y"

# starting the first data entry loop for boxes
while box_continue == ("y" or "Y"):
    number_of_taws = int(input("Please enter the number of taws [10 or more]:  "))  # getting information about number of taws in the every box
    while number_of_taws < 10:
        number_of_taws = int(input("Invalid entry, please enter again [10 or more]: "))

    weight_of_taw = int(input("Please enter weight of the taw in milligram: "))  # weight of first taw
    total_taw_weight += weight_of_taw
    default_weight = weight_of_taw  # defining default weight
    temp_weight = weight_of_taw  # defining temporary weight
    for i in range(number_of_taws - 1):  # main checking loop
        rep += 1
        weight_of_taw = int(input("Please enter weight of the taw in milligram: "))
        total_taw_weight += weight_of_taw
        # checking for box quality (valid or invalid)
        if weight_of_taw != default_weight:
            different_weight = weight_of_taw
            diff_counter += 1
        if weight_of_taw == temp_weight:
            continuous_num += 1

        else:
            continuous_num = 0
        if diff_counter > 1 and continuous_num + 1 != rep:
            print("There is a manufacturing defect in that box!")
            valid_box = False
            returned_taws += number_of_taws
            returned_boxes += 1
            break
        temp_weight = weight_of_taw
        if diff_counter == 0:  # all equal boxes
            if number_of_taws > largest_number_of_taws:
                largest_number_of_taws = number_of_taws
                largest_weight_of_taw = weight_of_taw
            if weight_of_taw > heaviest_weight_of_taw:
                heaviest_weight_of_taw = weight_of_taw
                heaviest_number_of_taws = number_of_taws
    if valid_box:  # in valid boxes making calculations and checking for how the boz is valid
        print("This is a valid box!")
        accepted_taws += number_of_taws
        accepted_boxes += 1
        if diff_counter == 0:  # all equal boxes
            print("All taws are equal in this box!")
            same_weight_boxes += 1
        else:  # one lighter or heavier boxes
            if diff_counter == number_of_taws - 1:
                different_weight = default_weight
                default_weight = weight_of_taw
                if default_weight > different_weight:
                    light_taw_weight = total_taw_weight
                    lighter_boxes += 1
                    weight_difference = abs(different_weight - default_weight)
                    total_difference_lighter += weight_difference
                    print(f"There is one taw in this box lighter than the others and the value difference is {weight_difference:.2f} and the percentage of difference is %{(weight_difference / default_weight * 100):.2f}")
                elif default_weight < different_weight:
                    heavy_taw_weight = total_taw_weight
                    heavier_boxes += 1
                    weight_difference = abs(default_weight - different_weight)
                    total_difference_heavier += weight_difference
                    print(f"There is one taw in this box heavier than the others and the value difference is {weight_difference:.2f} and the percentage of difference is %{(weight_difference / default_weight * 100):.2f}")
            else:
                if default_weight < different_weight:
                    heavy_taw_weight = total_taw_weight
                    heavier_boxes += 1
                    weight_difference = abs(default_weight - different_weight)
                    total_difference_heavier += weight_difference
                    print(f"There is one taw in this box heavier than the others and the value difference is {weight_difference:.2f} and the percentage of difference is %{(weight_difference / default_weight * 100):.2f}")
                elif default_weight > different_weight:
                    light_taw_weight = total_taw_weight
                    lighter_boxes += 1
                    weight_difference = abs(different_weight - default_weight)
                    total_difference_lighter += weight_difference
                    print(f"There is one taw in this box lighter than the others and the value difference is {weight_difference:.2f} and the percentage of difference is %{(weight_difference / default_weight * 100):.2f}")
        # defining difference in all boxes
        if abs(different_weight - default_weight) > max_difference:
            if different_weight == 0:
                max_difference = max_difference
            else:
                max_difference = abs(different_weight - default_weight)
                percentage_calculator_max = (default_weight + different_weight) / PERCENTAGE_DIVIDER  # making calculation about percentage
            if different_weight - default_weight > 0:
                max_sign = "Heavy"
            else:
                max_sign = "Light"
        # defining difference in all boxes
        if abs(different_weight - default_weight) < min_difference:
            percentage_calculator_min = (default_weight + different_weight) / PERCENTAGE_DIVIDER  # making calculation about percentage
            min_difference = abs(different_weight - default_weight)
            if different_weight - default_weight > 0:
                min_sign = "Heavy"
            else:
                min_sign = "Light"

    # resetting for the new calculations
    all_boxes = accepted_boxes + returned_boxes
    different_weight = 0
    default_weight = 0
    diff_counter = 0
    continuous_num = 0
    rep = 0
    valid_box = True
    box_continue = input("Do you want to continue to add boxes? [y/Y - n/N]: ")  # continuing the loop

# all printing part for requested data
print(f"There are {returned_boxes} boxes that have manufacturing defect and percentage is %{(returned_boxes / all_boxes * 100):.2f}")
print(f"There are {accepted_taws} accepted taws and there are {returned_taws} returned taws in total")
print(f"There are {same_weight_boxes} boxes that all taws in that box are equal and the percentage is %{(same_weight_boxes / accepted_boxes * 100):.2f}")
print(f"There are {lighter_boxes} boxes that one taw in that box is lighter than the others and the percentage is %{(lighter_boxes / accepted_boxes * 100):.2f}")
print(f"There are {heavier_boxes} boxes that one taw in that box is heavier than the others and the percentage is %{(heavier_boxes / accepted_boxes * 100):.2f}")
print(f"Average of weight difference of heavier boxes is {(total_difference_heavier / heavier_boxes):.2f} and the percentage is %{(total_difference_heavier / ((total_difference_heavier+heavy_taw_weight)/PERCENTAGE_DIVIDER) * 100):.2f} ")
print(f"Average of weight difference of lighter boxes is {(total_difference_lighter / lighter_boxes):.2f} and the percentage is %{(total_difference_lighter / ((total_difference_lighter+light_taw_weight)/PERCENTAGE_DIVIDER) * 100):.2f}")
print(f"Among the boxes in which all taws are of equal weight, the number of taws in the box with the largest number of taws is {largest_number_of_taws} and the weight of 1 taw in that box is {largest_weight_of_taw} ")
print(f"Among the boxes in which all taws are of equal weight, the number of taws in the box with the heaviest taws is {heaviest_number_of_taws} and the weight of 1 taw in that box is {heaviest_weight_of_taw}")
print(f"The value of max difference is {max_difference:.2f}, the percentage is %{(max_difference/ percentage_calculator_max * 100):.2f} and the sign is {max_sign}")
print(f"The value of min difference is {(abs(min_difference)):.2f}, the percentage is %{((abs(min_difference))/ percentage_calculator_min * 100):.2f} and the sign is {min_sign}")
