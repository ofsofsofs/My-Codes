# player personal inputs
age = int(input("Please enter your age:"))
last_annual_fee = float(input("Please enter your last annual fee:"))
team_place = int(input("Please enter your team place:"))

# defining cost without playoff games
cost = last_annual_fee / 26

# team part that didn't play playoffs
if team_place > 8:
    if age < 22:
        print(f"Your cost to your team per game you play: {cost:.2f}")
        print("You can't leave your team!")
    elif age == 22:
        print(f"Your cost to your team per game you play: {cost:.2f}")
        print(f"You have the right to be released (leave your team), your release fee: ${last_annual_fee * 2:.2f}")
    elif age == 23:
        print(f"Your cost to your team per game you play: {cost:.2f}")
        print(f"You have the right to be released (leave your team), your release fee: ${last_annual_fee:.2f}")
    elif age == 24:
        print(f"Your cost to your team per game you play: {cost:.2f}")
        print(f"You have the right to be released (leave your team), your release fee: ${last_annual_fee / 2:.2f}")
    else:
        print(f"Your cost to your team per game you play: {cost:.2f}")
        print(f"You have the right to be released (leave your team), your release fee: $0.00")

# team part that played playoffs
else:
    playoff_game_played = int(input("Please enter game count you played in playoffs:"))
    cost_play_off = last_annual_fee / (26 + playoff_game_played)  # defining cost with playoff games
    if age < 21:
        print(f"Your cost to your team per game you play: {cost_play_off:.2f}")
        print("You can't leave your team!")
    elif age == 22:
        print(f"Your cost to your team per game you play: {cost_play_off:.2f}")
        print(f"You have the right to be released (leave your team), your release fee: ${last_annual_fee * 2:.2f}")
    elif age == 23:
        print(f"Your cost to your team per game you play: {cost_play_off:.2f}")
        print(f"You have the right to be released (leave your team), your release fee: ${last_annual_fee:.2f}")
    elif age == 24:
        print(f"Your cost to your team per game you play: {cost_play_off:.2f}")
        print(f"You have the right to be released (leave your team), your release fee: ${last_annual_fee / 2:.2f}")
    else:
        print(f"Your cost to your team per game you play: {cost_play_off:.2f}")
        print(f"You have the right to be released (leave your team), your release fee: $0.00")
