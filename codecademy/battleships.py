from random import randint
board = [] #length of elements is col. number of elements is row.

ships_coordinates = []
number_of_ships = 8
row = 8
col = 8
tries = 6
    
def tidy_board(board): #display user-friendly board
    for e in board:
        print " ".join(e)

def placeship(board,ship_coordinates):  #to modify board to display where ships
    '''
    r = row
    c = col
    '''
    coordinates_set = []
    
    for coordinate in ship_coordinates:
        board[(coordinate[0]-1)][(coordinate[1]-1)] = 'S'
        coordinates_set.append(coordinate)
    
    count = 0
    for coordinate in coordinates_set:
        count+=1
        print "{}. ship placed at {} and ready for battle, sir!" .format(count,coordinate)

def attack(point,board):
    '''
    point : a coordinate [x.y]
    '''
    if board[point[0]-1][point[1]-1] == 'S':
        board[point[0]-1][point[1]-1] = 'X'
        print '\n','it\'s a hit!'
        return tidy_board(board)
    else:
        board[point[0]-1 ][point[1]-1] = 'M'
        print '\n', 'you missed'
        return tidy_board(board)    

def endgame(board):
    print '----------', 'END GAME STATS', '----------'
    count = 0 #number of ships left
    for row in board:
        for coordinate in row:
            if 'S' == coordinate:
                count +=1
    score = float(count)/number_of_ships
    if score ==0:
        return 'You win, commander.'
    elif score <= .25:
        return 'Several enemy vessels still lurk in your area, but it can be solved. Hang tight commander!'
    else:
        return 'You lose!'

#set up
#create board
for i in range(row):
    board.append(['0']*col)

#create ships

while len(ships_coordinates) < number_of_ships:
    coordinate = []
    
    row_coordinate = randint(1,row)
    col_coordinate = randint(1,col)
    
    coordinate.append(row_coordinate)
    coordinate.append(col_coordinate)
    
    if coordinate in ships_coordinates: #duplicate found. Not appended to ships_coordinates.
        pass
    else:
        ships_coordinates.append(coordinate)
    
#starting scenario

print placeship(board,ships_coordinates)
print tidy_board(board)

#attack phase

try_count = 0


#attacks with limited tries

while tries - try_count != 0:
    print 'try number', try_count +1
    point = []
    coordinate = raw_input('you wish to attack coordinate (row,col): ')
    
    while int(coordinate[0]) > row or int(coordinate[1]) > col: #if coordintate is outside playzone
        coordinate = raw_input('Sorry, please input again: ')
        
    for i in coordinate:
        point.append(int(i))

    attack(point,board)
    try_count +=1
    
    
#end phase
print endgame(board)
