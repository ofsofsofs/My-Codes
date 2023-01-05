valid_move_row = "n"
while valid_move_row == "n":
    if row_dic[(move_list[0][0])] > row_dic[(move_list[0][3])]:
        for i in range(1, row_dic[(move_list[0][0])] - row_dic[(move_list[0][3])] + 1):
            if game_board[row_dic[(move_list[0][0])] - i][column_dic[(move_list[0][1])]] != '':
                move_list.clear()
                move = input(
                    f"Invalid entry, there is another stone in that location, player {player_one_char}, please enter the position of your own stone you want to move and the target position:")
                move_list.append(move)
        else:
            valid_move_row = "y"
    else:
        for i in range(1, row_dic[(move_list[0][0])] - row_dic[(move_list[0][3])] + 1):
            if game_board[row_dic[(move_list[0][0])] + i][column_dic[(move_list[0][1])]] != '':
                move_list.clear()
                move = input(
                    f"Invalid entry, there is another stone in that location, player {player_one_char}, please enter the position of your own stone you want to move and the target position:")
                move_list.append(move)
        else:
            valid_move_row = "y"
valid_move_col = "n"
while valid_move_col == "n":
    if column_dic[(move_list[0][1])] > column_dic[(move_list[0][4])]:
        for i in range(1, column_dic[(move_list[0][1])] - column_dic[(move_list[0][4])] + 1):
            if game_board[row_dic[(move_list[0][0])]][column_dic[(move_list[0][1])] - i] != '':
                move_list.clear()
                move = input(
                    f"Invalid entry, there is another stone in that location, player {player_one_char}, please enter the position of your own stone you want to move and the target position:")
                move_list.append(move)
        else:
            valid_move_col = "y"
    else:
        for i in range(1, column_dic[(move_list[0][1])] - column_dic[(move_list[0][4])] + 1):
            if game_board[row_dic[(move_list[0][0])]][column_dic[(move_list[0][1])] + i] != '':
                move_list.clear()
                move = input(
                    f"Invalid entry, there is another stone in that location, player {player_one_char}, please enter the position of your own stone you want to move and the target position:")
                move_list.append(move)
        else:
            valid_move_col = "y"