#STEP_1

#STEP_1.1

from IPython.display import clear_output
# Из библиотеки IPython.display импортирую метод clear_output, который очищает
# доску каждый раз перед созданием новой игры

def display_board(board):    # Создаю доску
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


#STEP_1.2

# Создаю функцию выбора игроком крестика или нолика

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


#STEP_1.3

# Функция которая берет на доске маркер и назначает этот маркер на выбранную игроком позицию

def place_marker(board, marker, position):
    board[position] = marker

# STEP_1.4

# Функция которая принимает доску в качестве аргумента и проверяет кто победитель (?! *** разобрать!)

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


# STEP_1.5

# Импорт модуля random и функция определяющая, случайным образом, кто из игроков ходит первым.

import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


#STEP_1.6

# функция возвращающая результат проверки свободна-ли выбранная позиция

def space_check(board, position):
    return board[position] == ' '

#STEP_1.7

# функция, проверяющая заполнена-ли доска

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#STEP_1.8

# Функция, которая запрашивает следующую позицию игрока (как число 1-9),
# а затем использует функцию из шага 6, чтобы проверить, свободна ли она.
# Если это так, возвращает позицию для дальнейшего использования.

def player_choice(board):
    # Using strings because of raw_input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9) ')
    return int(position)

#STEP_1.9

# Функция спрашивает игока будет-ли он продолжать игру

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


#STEP_2.10

# ЗАПУСК ИГРЫ

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

