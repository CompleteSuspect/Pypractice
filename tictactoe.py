import random
def game(): #game logic
    player_x, player_o, grid = start_game()
    if random.randrange(1,7) % 2 == 1:
        player_1, player_2 = player_x, player_o
    else:
        player_1, player_2 = player_o, player_x
    print(f'{player_1[0]}, you go first.')
    draw(grid)

    move_counter = 0

    while True:
        play(player_1,grid)# place marker
        draw(grid)#display grid on screen
        move_counter += 1
        if win_check(player_1,grid): #check for a win
            return None
        if move_counter == 9:
            print('No more moves available')
            return None


        play(player_2,grid)
        draw(grid)
        move_counter += 1
        if win_check(player_2,grid):
            return None
        if move_counter == 9:
            print('No more moves available')
            return None

def start_game(): # sets a new game
    grid = dict(a = {'1':None, '2':None ,'3':None}
               ,b = {'1':None, '2':None ,'3':None}
               ,c = {'1':None, '2':None, '3':None}
               )
    while True:
        valid_check = 0

        while valid_check < 1:
            player_x = input('X. Please enter your name: '), 'X' #tuple (player_name, 'X')
            if player_x[0] == '' or player_x[0] == ' ':
                print('Please enter a valid name.')
                continue
            else:
                valid_check = 1

        while valid_check < 2:
            player_o = input('O. Please enter your name: '), 'O' # tuple (player_name, 'O')
            if player_o[0] == '' or player_o[0] == ' ':
                print('Please enter a valid name')
                continue
            else:
                valid_check = 2

        if player_x[0] == player_o[0]:
            print('Please enter different names')
            continue
        else:
            return (player_x, player_o, grid)

def play(player,grid): # Add a marker to the game grid, and detects bad inputs
    while True:
        move_pos = list(input(f"{player[0]}, please enter a grid position to place '{player[1]}': ").lower()) #player chooses a position

        if len(move_pos) == 2:
            if 'a' in move_pos or 'b' in move_pos or 'c' in move_pos[0]:
                if '1' in move_pos or '2' in move_pos or '3' in move_pos[1]:
                    if grid[move_pos[0]][move_pos[1]] is None: # check if position is empty
                        grid[move_pos[0]][move_pos[1]] = player[1] # adds marker to the grid dictionary
                        return None
                    else:
                        print(f'Position {move_pos[0]}{move_pos[1]} is not empty.')
                else:
                    print('Invalid position.')
        else:
            print('Invalid position.')

def win_check(player,grid): #checks for a horizontal, vertical or diagonal win

    if h_win_check(player,grid):
        print(f'{player[0]} has a horizontal win!')
        return True
    if v_win_check(player, grid):
        print(f'{player[0]} has a vertical win!')
        return True
    if d_win_check(player, grid):
        print(f'{player[0]} has a diagonal win!')
        return True


def h_win_check(player, grid): # checks for a horizontal win
    column_lst = [column for column in grid]

    for row in range(1,4):
        score_accum = 0

        for column in column_lst:

            if grid[column][str(row)] == player[1]:
                score_accum += 1

        if score_accum == 3:
            return True

def v_win_check(player,grid): # checks for a vertical win
    column_lst = [column for column in grid]

    for column in column_lst:
        score_accum = 0

        for row in range(1,4):

            if grid[column][str(row)] == player[1]:
                score_accum += 1

        if score_accum == 3:
            return True

def d_win_check(player,grid): # checks for a diagonal win
    column_lst = [column for column in grid]

    diag = zip(column_lst, range(1,4))
    score_accum = 0

    for column, row in diag:

        if grid[column][str(row)] == player[1]:
            score_accum += 1

        if score_accum == 3:
            return True

    diag = zip(column_lst[::-1], range(1,4))
    score_accum = 0

    for column, row in diag:
        if grid[column][str(row)] == player[1]:
            score_accum += 1

        if score_accum == 3:
            return True

def draw(grid): # visual view of the grid:
    marker_lst = []
    column_lst = [column for column in grid]
    for row in range(1,4):
        for column in column_lst:
            if grid[column][str(row)] is None:
                marker_lst.append(' ')
            else:
                marker_lst.append(grid[column][str(row)])

    print('        A        B       C   \n'
          '             |       |       ')

    print('    1    {}   |   {}   |   {}'.format(marker_lst[0], marker_lst[1], marker_lst[2]).rstrip())

    print('      _______|_______|_______\n'
          '             |       |       ')

    print('    2    {}   |   {}   |   {}'.format(marker_lst[3], marker_lst[4], marker_lst[5]).rstrip())

    print('      _______|_______|_______\n'
          '             |       |       ')

    print('    3    {}   |   {}   |   {}'.format(marker_lst[6], marker_lst[7], marker_lst[8]).rstrip())

    print('             |       |       ')


def reset(): # Asks user for another game

    again = input('Play again? ').lower()

    if again == 'yes' or again == 'y':
        return True

while True:
    game()
    if reset():
        continue
    else:
        break
