def Board():
    numrows = 3
    
    #Generate 2d-grid-array with empty space as placeholder for elements
    board = [['   '] * (numrows + 2) for _ in range(numrows + 2)]
    
    #Add borders to the odd numbered rows and columns
    for row in range(numrows + 2):
        for col in range(numrows + 2):
            if row %  2 == 1:
                board[row][col] = '___'
            if col % 2 == 1:
                board[row][col] = '|'
    
    #Add last set of column borders in the last row 
    board.append(['   '] * (numrows + 2))
    board[numrows + 2][1] = '|'
    board[numrows + 2][3] = '|'
    
    return board


def printBoard(board):
    #Print formatted Board
    for row in board:
        print(''.join(row))
    return board


def player(playerpiece, board, movesmap):
    #Initiate and input player move, making sure it is a number from 1 to 9
    while True:
        playerpos = '0'
        while playerpos not in '123456789' or playerpos == '':
            playerpos = input('Please enter a number from 1 to 9 to place your piece on the board: ')
            print('\n')
            playerCoord = movesmap.get(int(playerpos))
    
        '''Check board position is not already occupied before placing piece.
        If occupied, then ask player for another move'''
        if board[playerCoord[0]][playerCoord[1]] == '   ':
            board[playerCoord[0]][playerCoord[1]] = playerpiece
            printBoard(board)
            return board
        else:
            print('Position Occupied. Try another move.')


def victoryCheck(board):
    #Checks victory conditions for the game by checking board
    lenboa = len(board)
    
    #List representing the win for each piece (player)--X and O
    winx = [' X '] * (len(board) - 3)
    wino = [' O '] * (len(board) - 3)
    
    #Win conditions: Horizontal, Vertical, Main Diagonal, Other Diagonal
    winh = [[board[i][j] for j in range(0, lenboa, 2)] for i in range(0, lenboa, 2)]
    winv = [[board[j][i] for j in range(0, lenboa, 2)] for i in range(0, lenboa, 2)]
    winmdiag = [board[i][i] for i in range(0, lenboa, 2)]
    winodiag = [board[(lenboa - 2) - i][i] for i in range(0, lenboa, 2)]
    
    
    if winmdiag == winx or winmdiag == wino:
        return True
    elif winodiag == winx or winodiag == wino:
        return True
    for i in range(len(winh)):
        if winh[i] == winx or winh[i] == wino:
            return True
        if winv[i] == winx or winv[i] == wino:
            return True
    else:
        return False


def instructRules():
    #Initiate instructional board showing what user can input for moves
    instboard = Board()
    
    i = 0
    for row in range(0, len(instboard), 2):
        instboard[row][0] = ' ' + str(row + (i + 1)) + ' '
        instboard[row][2] = ' ' + str(row + 2 + i) + ' '
        instboard[row][4] = ' ' + str(row + 4 + (i - 1)) + ' '
        i += 1
    
    print('The following board indicates all the valid positions you can enter:\n')
    printBoard(instboard)
    
    return instboard
    

def getMovesMap(board): 
    '''Build dictionary mapping single digit user input to board position; return
    movesmap so that we can use dictionary to map user input for moves'''
    
    movesmap = {}
    i = 0
    for row in range(0, len(board), 2):
        movesmap[row + (i + 1)] = [row, 0]
        movesmap[row + 2 + i] = [row, 2]
        movesmap[row + 4 + (i - 1)] = [row, 4]
        i += 1
    
    return movesmap



def playTicTacToe():
    #Game Input Instructions for Tic-Tac-Toe, i.e. what users input to define move
    instruct = instructRules()
    
    #Start of the game, printing empty board and instructions
    print("\n\nLet's play Tic-Tac-Toe!\n")
    board = Board()
    printBoard(board)
    movesmap = getMovesMap(board)
    
    #Player 1 is X and player 2 is O
    print('\nPlayer 1 plays piece X. Player 2 plays piece O.')
    p1piece = ' X '
    p2piece = ' O '
    
    turns = 0
    while not victoryCheck(board):
        turns += 1
        print("\n\nTurn--Player 1!\n")
        printBoard(instruct)
        player1 = player(p1piece, board, movesmap)
        if victoryCheck(board) == True:
            print("\nGame Over! Player 1 Wins!")
            break
        
        #Check for draw--Tied--game condition
        if ((turns == 9) and (victoryCheck(board) == False)):
            print('\nDraw! Game Over.')
            break
        
        turns += 1
        print("\n\nTurn--Player 2!\n")
        printBoard(instruct)
        player2 = player(p2piece, board, movesmap)
        if victoryCheck(board) == True:
            print('\nGame Over! Player 2 Wins!')
            
    return None


playTicTacToe()