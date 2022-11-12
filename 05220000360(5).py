# defining all names for calculations and usage
total_points_won = 0
total_points_lost = 0
match_points_won = 0
match_points_lost = 0
set_won = 0
set_lost = 0
set_played = 0
five_set_played = 0
season_points_won = 0
season_points_lost = 0
no_set_lost_win = 0
match_won = 0
match_lost = 0
points_difference = 0
max_points_difference = 0
most_difference_team_name = ""

match_played = int(input("How many matches did you play? "))
for x in range(1, match_played+1):
    team_name = input("Please enter the opposing team name: ")  # getting input from user to start program
    for i in range(1, 6):
        points_won = int(input("Please enter the number of points you won: "))  # getting input from user to start program
        points_lost = int(input("Please enter the number of points you lost: "))  # getting input from user to start program
        # checking for did team lose the set or win the set
        if points_won > points_lost:
            set_won += 1
        else:
            set_lost += 1
        set_played = set_won + set_lost

        if (set_won == 3 and set_lost == 2) or (set_won == 2 and set_lost == 3):  # there is a request from a user so need to find that info
            five_set_played += 1

        # the calculations part for printing
        match_points_won += points_won
        match_points_lost += points_lost
        total_points_won += points_won
        total_points_lost += points_lost
        season_points_won += total_points_won
        season_points_lost += total_points_lost

        total_points_lost = 0  # resetting for new calculations
        total_points_won = 0  # resetting for new calculations

        if set_won == 3 and set_lost == 0:
            no_set_lost_win += 1  # calculating winnings with no set lose
        if set_won == 3 or set_lost == 3:
            break
        # the part that I find maximum difference between teams
    points_difference += match_points_won - match_points_lost
    if abs(points_difference) > abs(max_points_difference):
        max_points_difference = points_difference
        most_difference_team_name = team_name
    points_difference = 0

    if set_won > set_lost:
        match_won += 1  # calculating matches that team won
    else:
        match_lost += 1  # calculating matches that team lost

# printing part for each match
    print(f"The number of points won in match is {match_points_won}")
    print(f"The number of points lost in match is {match_points_lost}")
    print(f"The number of sets won in match is {set_won}")
    print(f"The number of sets lost in match is {set_lost}")
    print(f"The average of points won per set is {(match_points_won/set_played):.2f} and points lost per set is {(match_points_lost/set_played):.2f}")

# resetting for to calculate every match
    set_won = 0
    set_lost = 0
    match_points_won = 0
    match_points_lost = 0

# printing part for all matches(season)
print(f"The total number of points won in season is {season_points_won} and the average of points won per match is {season_points_won / match_played}")
print(f"the number of matches won is {match_won} and the lost is {match_lost}")
print(f"The number of matches won without losing a set is {no_set_lost_win} and the percentage is %{no_set_lost_win * 100 / match_won}")
print(f"The number of matches finished in 5 set is {five_set_played} and percentage in all matches is %{(five_set_played * 100 / match_played):.2f}")
print(f"The highest difference between the total points won and the total points lost is {abs(max_points_difference)} and the opposing team name is {most_difference_team_name}")
