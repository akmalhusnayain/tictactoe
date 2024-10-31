game_list = [0,1,2]

def display_game(game_list):
    print('here is the current game')
    print(game_list)

def position_choice():
    choice = 'wrong'

    while choice not in ['0','1','2']:
        choice = input('pick a position (0, 1, 2): ')

        if choice not in ['0','1','2']:
            print('Sorry, invalid choice!')
    
    return int(choice)

def replacement_choice(game_list,posittion):

    user_replacement = input('type a string to place at position: ')

    game_list[posittion] = user_replacement

    return print(game_list)

replacement_choice(game_list,1)

