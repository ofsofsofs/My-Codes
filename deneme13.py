marble_count = int(input("How many marbles are in the box?"))

marble_weight = int(input("Weight of marble: "))
default_weight = marble_weight
temp_weight = marble_weight
diff_count = 0
continuous_num = 0
rep = 0
valid_box = True
for i in range(marble_count - 1):
    rep += 1
    marble_weight = int(input("Weight of marble: "))
    if marble_weight != default_weight:
        diff_count += 1

    if marble_weight == temp_weight:
        continuous_num += 1
    else:
        continuous_num = 0

    if diff_count > 1 and continuous_num + 1 != rep:
        print("Invalid box")
        valid_box = False
        break

    temp_weight = marble_weight
    print("Temp weight:", temp_weight, "\n",
          "diff count:", diff_count, "\n",
          "con num:", continuous_num, "rep:", rep)


if valid_box:
    print("VALID BOX")