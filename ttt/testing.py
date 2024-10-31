def player_input():
    choice = 'wrong'

    while choice not in ['X','O']:
        choice = input('pick X or O: ')

        if choice not in ['X','O']:
            print('Sorry, invalid choice!')
    
    return choice

def place_marker(board, marker, position):
    player_input()
    user_replacement = int(input('Please enter a number'))

    board[position] = user_replacement
  



    