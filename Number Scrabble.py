welcome_message = '''welcome to Number scrabble
Number scrabble is played with the list of numbers between 1 and 9. Each player takes
turns picking a number from the list. Once a number has been picked, it cannot be picked
again. If a player has picked three numbers that add up to 15, that player wins the game.
However, if all the numbers are used and no player gets exactly 15, the game is a draw.'''
print(welcome_message)

from itertools import combinations


def gameplay():
    choices = ['Y', 'N']
    while True:
        player_choice = input("would you like to play again? (y/n): ").upper()
        if player_choice not in choices:
            print("please select a valid choice (y/n)")
            continue
        break
    return player_choice


# check if the sum of 3 numbers = 15
def winner_check(player_values):
    if len(player_values) > 2:
        comb_list = list(combinations(player_values, 3))
        for comb in comb_list:
            sum = 0
            for i in comb:
                i = int(i)
                sum = sum + i
            if sum == 15:
                return "T"


# check valid input
def validity(play_choice, game_list):
    if play_choice not in game_list:
        return "F"
    else:
        return "T"


def update_game_status(player_number,lst,play_choice):
    player_number.append(play_choice)
    lst.remove(play_choice)


def reset_game_status():
    global start_list, player1_values, player2_values, player1, player2
    start_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player1_values = []
    player2_values = []
    player1 = input("Player 1 name : ")
    player2 = input("Player 2 name : ")


reset_game_status()
while True:
    # ask player1 for number & check for validity
    while True:
        player1_choice = input(f"{player1} please pick a number from {start_list} : ")
        if validity(player1_choice, start_list) == "F":
            print("you picked a chosen/invalid number!, please pick another one.")
        else:
            break

    # update game status
    update_game_status(player1_values,start_list,player1_choice)

    print(f"{player1} picked : {player1_values}---{player2} picked : {player2_values}")
    # check for winner/draw
    if winner_check(player1_values) == "T":
        print(f"Congratulations, {player1}, on your victory! Well done!")
        if gameplay() == 'Y':
            reset_game_status()
            continue
        else:
            break

    if start_list == []:
        print("The game ends in a draw. Well played by both sides!")
        if gameplay() == 'Y':
            reset_game_status()
            continue
        else:
            break

    # ask player1 for number & check for validity
    while True:
        player2_choice = input(f"{player2} please pick a number from {start_list} : ")
        if validity(player2_choice, start_list) == "F":
            print("you picked a chosen/invalid number!, please pick another one.")
        else:
            break

    # update game status
    update_game_status(player2_values, start_list, player2_choice)

    # check for winner/draw
    print(f"{player1} picked : {player1_values}---{player2} picked : {player2_values}")
    if winner_check(player2_values) == "T":
        print(f"Congratulations, {player2}, on your victory! Well done!")
        if gameplay() == 'Y':
            reset_game_status()
            continue
        else:
            break

    if start_list == []:
        print("The game ends in a draw. Well played by both sides!")
        if gameplay() == 'Y':
            reset_game_status()
            continue
        else:
            break


