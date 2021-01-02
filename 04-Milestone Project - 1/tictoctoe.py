import os
import random
import collections
from subprocess import call
#from IPython.display import clear_output


def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')
    #clear_output()


# display tic toc toe board
def display_board(board):
    print(' ' + ' ' + ' | ' + ' ' + ' | ' + ' ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + ' ' + ' | ' + ' ' + ' | ' + ' ')

    print('_'*11)
    print(' ' + ' ' + ' | ' + ' ' + ' | ' + ' ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + ' ' + ' | ' + ' ' + ' | ' + ' ')

    print('_'*11)
    print(' ' + ' ' + ' | ' + ' ' + ' | ' + ' ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' ' + ' ' + ' | ' + ' ' + ' | ' + ' ')


# get player input
def player_input():
    player1 = ''
    player2 = ''

    while player1.upper() not in ['X', 'O']:
        player1 = input("Please pick a marker 'X' or 'O': ")

        if player1.upper() not in ['X', 'O']:
            print("Sorry, I don't understand your input. Please choose X or O! ")

        if player1.upper() == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

    return (player1.upper(), player2.upper())


# place the marker in the given position within the board
def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, marker):
    if collections.Counter([board[1], board[2], board[3]]) == collections.Counter([marker, marker, marker]):
        return True
    elif collections.Counter([board[4], board[5], board[6]]) == collections.Counter([marker, marker, marker]):
        return True
    elif collections.Counter([board[7], board[8], board[9]]) == collections.Counter([marker, marker, marker]):
        return True
    elif collections.Counter([board[1], board[4], board[7]]) == collections.Counter([marker, marker, marker]):
        return True
    elif collections.Counter([board[2], board[5], board[8]]) == collections.Counter([marker, marker, marker]):
        return True
    elif collections.Counter([board[3], board[6], board[9]]) == collections.Counter([marker, marker, marker]):
        return True
    elif collections.Counter([board[1], board[5], board[9]]) == collections.Counter([marker, marker, marker]):
        return True
    elif collections.Counter([board[7], board[5], board[3]]) == collections.Counter([marker, marker, marker]):
        return True

    return False


# decide which player go first
def choose_first():
    return random.randint(1, 2)

# decide if we have a empty space


def space_check(board, position):
    if board[position] not in ['X', 'O']:
        return True
    else:
        return False

# check board is full


def full_board_check(board):
    for position in range(1, len(board)+1):
        if space_check(board, position) == True:
            return False

    print("Nobody won. Please try again..")
    return True


# get player next move and return the position if it's available
def player_choice(board):
    choice = ''
    within_range = False
    while choice.isdigit() == False and within_range == False:
        choice = input("Please choose you next position (as a number 1-9)): ")

        if choice.isdigit() == False:
            choice = input("Please choose you next position (as a number 1-9): ")
        elif int(choice) not in range(1, 10):
            print("Choose correctly your next position (as a number 1-9): ")
            within_range = False
        else:
            within_range = True
            if space_check(board, int(choice)) == True:
                return int(choice)
            else:
                return 0

# do you whan to play again?


def replay():
    choise = ''

    while choise.upper() not in ['Y', 'N']:
        choise = input("Do you what to play again. Please answer with Y or N: ")

        if choise.upper() not in ['Y', 'N']:
            print("Please answer with Y or N! ")
        else:
            if choise.upper == 'Y':
                return True
            else:
                return False

# play TicTacToe
clear()
print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    game_on = True
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # choose who is starting first
    first_player = choose_first()
    if first_player == 1:
        print('Player 1 will start first')
    else:
        print('Player 2 will start first')
        
    # get player input
    players = ('', '')
    players = player_input()
    player1 = players[0]
    player2 = players[1]
    print('Players choise: ')
    print(' - player1 ' + player1)
    print(' - player2 ' + player2)
    # start the game
    display_board(board)
    while game_on:
        # Player 1 Turn
        # clear()
        print('Player 1 ({}) Turn'.format(player1))
        position1 = player_choice(board)
        if position1 != 0:
            board = place_marker(board, player1, position1)
            display_board(board)
        # check playwer1 won
        if win_check(board, player1) == True:
            print('Player 1 ({}) won'.format(player1))
            game_on = False
            break
        # Player2's turn.
        # clear()
        print('Player 2 ({}) Turn'.format(player2))
        position2 = player_choice(board)
        if position2 != 0:
            board = place_marker(board, player2, position2)
            display_board(board)
        # check player2 won
        if win_check(board, player2) == True:
            print('Player 2 ({}) won'.format(player2))
            break
        if full_board_check(board) == True:
            game_on = False
            
    if not replay():
        break