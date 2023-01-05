def all_code():  # function for playing more than one time
    player_one_char = input("Please enter the first player's character: ")  # getting first player name
    while player_one_char == '':  # to avoid blank player name
        player_one_char = input("Invalid entry, please enter a letter or number: ")
    player_two_char = input("Please enter the second player's character: ")  # getting second player name
    while player_two_char == '':  # to avoid blank player name
        player_two_char = input("Invalid entry, please enter a letter or number: ")
    board_size = input("Please enter the size of game board [4 to 8]: ")

    while board_size != "4" and board_size != "5" and board_size != "6" and board_size != "7" and board_size != "8":  # getting board size
        board_size = input("Invalid entry, please enter again: ")

    row = int(board_size)
    side_name = ["A", "B", "C", "D", "E", "F", "G", "H"]  # defining side names

    # defining all dictionaries
    row_dic = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}
    column_dic = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    reverse_row_dic = {0: 1, 1: 2, 2: 3, 3: 4, 5: 6, 6: 7, 7: 8}
    reverse_column_dic = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}

    move_list = []  # creating empty list for player move
    game_board = [[' ' for i in range(row)] for i in range(row)]  # creating game board by board size
    # adding player one and two's chars to game board
    for j in range(row):
        for k in range(row):
            game_board[0][k] = player_two_char
            game_board[row-1][k] = player_one_char


    def printings():  # printing function that prints all the information
        print("  ", end="")
        for i in range(row):
            print(" ", side_name[i], "", end="")
            if i == row-1:
                print("")
        print(" ", "----"*row, end="")
        print("-")
        print("1", "| ", end="")
        for i in range(row):
            print(game_board[0][i], "| ", end="")
        print("1")
        l = 2
        while l != row+1:
            print(" ", "----" * row, end="")
            print("-")
            print(l, "| ", end="")
            if board_size == "4":
                print(game_board[l-1][0], "|", game_board[l-1][1], "|", game_board[l-1][2], "|", game_board[l-1][3], "|", end=" ")
            elif board_size == "5":
                print(game_board[l-1][0], "|", game_board[l-1][1], "|", game_board[l-1][2], "|",
                      game_board[l-1][3], "|", game_board[l-1][4], "|", end=" ")
            elif board_size == "6":
                print(game_board[l-1][0], "|", game_board[l-1][1], "|", game_board[l-1][2], "|",
                      game_board[l-1][3], "|", game_board[l-1][4], "|", game_board[l-1][5], "|", end=" ")
            elif board_size == "7":
                print(game_board[l-1][0], "|", game_board[l-1][1], "|", game_board[l-1][2], "|",
                      game_board[l-1][3], "|", game_board[l-1][4], "|", game_board[l-1][5], "|", game_board[l - 1][6], "|", end=" ")
            else:
                print(game_board[l-1][0], "|", game_board[l-1][1], "|", game_board[l-1][2], "|",
                      game_board[l-1][3], "|", game_board[l-1][4], "|", game_board[l-1][5], "|", game_board[l - 1][6], "|", game_board[l - 1][7], "|", end=" ")
            print(l)
            l += 1
        print(" ", "----" * row, end="")
        print("-")
        print("  ", end="")
        for i in range(row):
            print(" ", side_name[i], "", end="")
            if i == row - 1:
                print("")


    def moving_stones():  # function that takes player moves and checks for suitability
        while (sum(x.count(player_one_char) for x in game_board) != 1) and (sum(x.count(player_two_char) for x in game_board) != 1):  # if any players stone count become one game ends
            move = input(f"\nPlayer {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")  # getting player one's move
            while len(move) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                move = input(f"\nInvalid format, Player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
            move_list.append(move)
            while move_list[0][1] != move_list[0][4] and move_list[0][0] != move_list[0][3]:
                move_list.clear()
                move = input(f"\nInvalid entry, player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                while len(move) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                    move = input(f"\nInvalid format, Player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                move_list.append(move)
            for i in range(row_dic[(move_list[0][3])]+1, row_dic[(move_list[0][0])]):
                if game_board[i][column_dic[(move_list[0][1])]] != ' ':
                    move_list.clear()
                    move = input(f"\nInvalid entry, player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                    while len(move) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                        move = input(f"\nInvalid format, Player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                    move_list.append(move)
            for j in range(row_dic[(move_list[0][0])]+1, row_dic[(move_list[0][3])]):
                if game_board[j][column_dic[(move_list[0][1])]] != ' ':
                    move_list.clear()
                    move = input(f"\nInvalid entry, player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                    while len(move) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                        move = input(f"\nInvalid format, Player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                    move_list.append(move)
            for k in range(column_dic[(move_list[0][4])]+1, column_dic[(move_list[0][1])]):
                if game_board[row_dic[(move_list[0][0])]][k] != ' ':
                    move_list.clear()
                    move = input(f"\nInvalid entry, player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                    while len(move) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                        move = input(f"\nInvalid format, Player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                    move_list.append(move)
            for l in range(column_dic[(move_list[0][1])]+1, column_dic[(move_list[0][4])]):
                if game_board[row_dic[(move_list[0][0])]][l] != ' ':
                    move_list.clear()
                    move = input(f"\nInvalid entry, player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                    while len(move) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                        move = input(f"\nInvalid format, Player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                    move_list.append(move)
            while game_board[row_dic[(move_list[0][3])]][column_dic[(move_list[0][4])]] != ' ' or game_board[row_dic[(move_list[0][3])]][column_dic[(move_list[0][4])]] == player_two_char or game_board[row_dic[(move_list[0][0])]][column_dic[(move_list[0][1])]] != player_one_char:
                move_list.clear()
                move = input(f"\nInvalid entry, player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                while len(move) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                    move = input(f"\nInvalid format, Player {player_one_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                move_list.append(move)
            current_row = row_dic[(move_list[0][0])]  # current stone row index
            current_column = column_dic[(move_list[0][1])]  # current stone column index
            new_row = row_dic[(move_list[0][3])]  # new stone row index
            new_column = column_dic[(move_list[0][4])]  # new stone column idex
            game_board[current_row][current_column] = ' '  # removing current stone
            game_board[new_row][new_column] = player_one_char  # adding new stone
            locking()
            printings()
            move_list.clear()  # clearing it for new move
            current_row = 0  # clearing it for new move
            current_column = 0  # clearing it for new move
            new_row = 0  # clearing it for new move
            new_column = 0  # clearing it for new move
            if sum(x.count(player_one_char) for x in game_board) == 1:
                break
            elif sum(x.count(player_two_char) for x in game_board) == 1:
                break
            print(f"\nPLayer {player_one_char} has {sum(x.count(player_one_char) for x in game_board)} stones!")  # shows stones count
            print(f"PLayer {player_two_char} has {sum(x.count(player_two_char) for x in game_board)} stones!")  # shows stone count
            #  SAME CODE AS MOVE JUST FOR PLAYER TWO  #
            move2 = input(f"\nPlayer {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
            move_list.append(move2)
            while move_list[0][1] != move_list[0][4] and move_list[0][0] != move_list[0][3]:
                move_list.clear()
                move2 = input(f"\nInvalid entry, player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                while len(move2) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                    move2 = input(f"\nInvalid format, Player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                move_list.append(move2)
            for i in range(row_dic[(move_list[0][3])]+1, row_dic[(move_list[0][0])]):
                if game_board[i][column_dic[(move_list[0][1])]] != ' ':
                    move_list.clear()
                    move2 = input(f"\nInvalid entry, player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                    while len(move2) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                        move2 = input(f"\nInvalid format, Player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                    move_list.append(move2)
            for j in range(row_dic[(move_list[0][0])]+1, row_dic[(move_list[0][3])]):
                if game_board[j][column_dic[(move_list[0][1])]] != ' ':
                    move_list.clear()
                    move2 = input(f"\nInvalid entry, player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                    while len(move2) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                        move2 = input(f"\nInvalid format, Player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                    move_list.append(move2)
            for k in range(column_dic[(move_list[0][4])]+1, column_dic[(move_list[0][1])]):
                if game_board[row_dic[(move_list[0][0])]][k] != ' ':
                    move_list.clear()
                    move2 = input(f"\nInvalid entry, player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                    while len(move2) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                        move2 = input(f"\nInvalid format, Player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                    move_list.append(move2)
            for l in range(column_dic[(move_list[0][1])]+1, column_dic[(move_list[0][4])]):
                if game_board[row_dic[(move_list[0][0])]][l] != ' ':
                    move_list.clear()
                    move2 = input(f"\nInvalid entry, player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                    while len(move2) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                        move2 = input(f"\nInvalid format, Player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                    move_list.append(move2)
            while game_board[row_dic[(move_list[0][3])]][column_dic[(move_list[0][4])]] != ' ' or game_board[row_dic[(move_list[0][3])]][column_dic[(move_list[0][4])]] == player_one_char or game_board[row_dic[(move_list[0][0])]][column_dic[(move_list[0][1])]] != player_two_char:
                move_list.clear()
                move2 = input(f"\nInvalid entry, player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter]:")
                while len(move2) != 5:  # if users enter the move in wrong format this code detect it and gets move again
                    move2 = input(f"\nInvalid format, Player {player_two_char}, please enter the position of your own stone you want to move and the target position [number-letter][e.g. 1C 3C]:")
                move_list.append(move2)

            current_row = row_dic[(move_list[0][0])]
            current_column = column_dic[(move_list[0][1])]
            new_row = row_dic[(move_list[0][3])]
            new_column = column_dic[(move_list[0][4])]
            game_board[current_row][current_column] = ' '
            game_board[new_row][new_column] = player_two_char
            locking()
            printings()
            move_list.clear()
            current_row = 0
            current_column = 0
            new_row = 0
            new_column = 0
            if sum(x.count(player_one_char) for x in game_board) == 1:
                break
            elif sum(x.count(player_two_char) for x in game_board) == 1:
                break
            print(f"\nPLayer {player_one_char} has {sum(x.count(player_one_char) for x in game_board)} stones!")
            print(f"PLayer {player_two_char} has {sum(x.count(player_two_char) for x in game_board)} stones!")
        if sum(x.count(player_one_char) for x in game_board) == 1:  # prints winner player
            print(f"\nWinner is {player_two_char}")
            game_continue = input("Do you want to play again[y/n]: ")  # asks for new game
            if game_continue == "y" or game_continue == "Y":
                all_code()
        elif sum(x.count(player_two_char) for x in game_board) == 1:  # prints winner player
            print(f"\nWinner is {player_one_char}")
            game_continue = input("Do you want to play again[y/n]: ")  # asks for new game
            if game_continue == "y" or game_continue == "Y":
                all_code()


    def locking():  # checking all board for any locking
        for i in range(row):
            for j in range(row):
                if (i == 0 and j == 0) or (i == 0 and j == row-1) or (i == row-1 and j == 0) or (i == row-1 and j == row-1):  # checking corners
                    if i == 0 and j == 0:
                        if (game_board[i][j] == player_one_char) and (game_board[i+1][j] == player_two_char and game_board[i][j+1] == player_two_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                        elif (game_board[i][j] == player_two_char) and (game_board[i+1][j] == player_one_char and game_board[i][j+1] == player_one_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                    elif i == 0 and j == row-1:
                        if (game_board[i][j] == player_one_char) and (game_board[i+1][j] == player_two_char and game_board[i][j-1] == player_two_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                        elif (game_board[i][j] == player_two_char) and (game_board[i+1][j] == player_one_char and game_board[i][j-1] == player_one_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                    elif i == row-1 and j == 0:
                        if (game_board[i][j] == player_one_char) and (game_board[i-1][j] == player_two_char and game_board[i][j+1] == player_two_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                        elif (game_board[i][j] == player_two_char) and (game_board[i-1][j] == player_one_char and game_board[i][j+1] == player_one_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                    else:
                        if (game_board[i][j] == player_one_char) and (game_board[i-1][j] == player_two_char and game_board[i][j-1] == player_two_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                        elif (game_board[i][j] == player_two_char) and (game_board[i-1][j] == player_one_char and game_board[i][j+1] == player_one_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                elif j == 0 or j == row-1 or i == 0 or i == row-1:  # checks sides
                    if i == 0 or i == row-1:
                        if (game_board[i][j] == player_one_char) and (game_board[i][j-1] == player_two_char and game_board[i][j+1] == player_two_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                        elif (game_board[i][j] == player_two_char) and (game_board[i][j-1] == player_one_char and game_board[i][j+1] == player_one_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                    elif j == 0 or j == row-1:
                        if (game_board[i][j] == player_one_char) and (game_board[i-1][j] == player_two_char and game_board[i+1][j] == player_two_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                        elif (game_board[i][j] == player_two_char) and (game_board[i-1][j] == player_one_char and game_board[i+1][j] == player_one_char):
                            game_board[i][j] = ' '
                            print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                else:  # checks mid-parts
                    if game_board[i][j] == player_one_char and ((game_board[i+1][j] == player_two_char and game_board[i-1][j] == player_two_char) or (game_board[i][j+1] == player_two_char and game_board[i][j-1] == player_two_char)):
                        game_board[i][j] = ' '
                        print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")
                    elif game_board[i][j] == player_two_char and ((game_board[i+1][j] == player_one_char and game_board[i-1][j] == player_one_char) or (game_board[i][j+1] == player_one_char and game_board[i][j-1] == player_one_char)):
                        game_board[i][j] = ' '
                        print(f"\nThe stone at position {reverse_row_dic[i]}{reverse_column_dic[j]} was locked and removed.")


    def main():  # main function
        printings()
        moving_stones()


    main()


all_code()
