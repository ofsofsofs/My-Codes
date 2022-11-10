# first team inputs
first_team_name = str(input("Enter the name of the first team: "))
first_team_set = int(input("Enter the number of sets won by the first team: "))

# second team inputs
second_team_name = str(input("Enter the name of the second team: "))
second_team_set = int(input("Enter the number of sets won by the second team: "))

# defining part
first_team_point = int
second_team_point = int

# first team winnings
if first_team_set == 3 and second_team_set == 0:
    first_team_point = 3
    second_team_point = 0
if first_team_set == 3 and second_team_set == 1:
    first_team_point = 3
    second_team_point = 0
if first_team_set == 3 and second_team_set == 2:
    first_team_point = 2
    second_team_point = 1

# second team winnings
if second_team_set == 3 and first_team_set == 0:
    first_team_point = 0
    second_team_point = 3
if second_team_set == 3 and first_team_set == 1:
    first_team_point = 0
    second_team_point = 3
if second_team_set == 3 and first_team_set == 2:
    first_team_point = 1
    second_team_point = 2

# comparing and printing part
if first_team_point > second_team_point:
    print("The name of the team that won the match:", first_team_name, ", the team's point:", first_team_point)
    print("The name of the team that lose the match", second_team_name, ", the team's point", second_team_point)
if first_team_point < second_team_point:
    print("The name of the team that won the match:", second_team_name, ", the team's point:", second_team_point)
    print("The name of the team that lose the match", first_team_name, ", the team's point:", first_team_point)
