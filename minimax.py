from math import inf

def minimax(board, turn):
    bestmove = None
    #If somebody has won, return the winner
    for x in range(0,3):
        if board[x] == ["X", "X", "X"]:
            return (-1, None)
        if (board[0][x] == board[1][x] == board[2][x] == "X" != None):
            return (-1, None)
        if board[x] == ["O", "O", "O"] or board[0][x] == board[1][x] == board[2][x] == "O" != None: 
            return (1, None)
    if board[0][0] == board[1][1] == board[2][2] == "X" != None or board[0][2] == board[1][1] == board[2][0] == "X" != None:
        return (-1, None)
    if board[0][0] == board[1][1] == board[2][2] == "O" != None or board[0][2] == board[1][1] == board[2][0] == "O" != None:
        return (1, None)
    
    #If board is full - and the code makes it to this point, indicating that there is no winner - return draw
    if None not in board[0] and None not in board[1] and None not in board[2]: 
        return (0, None)
    
    if turn == "X": 
        value = 1
        moves = []
        for i in range (0,3):
            for j in range (0,3):
                if board[i][j] == None: 
                    moves.append({"row": i, "col":j})
        for move in moves: 
            board[move['row']][move['col']] = "X"
            value = min(value, minimax(board, "O")[0])
            board[move['row']][move['col']] = None
    if turn == "O":
        value = -1
        moves = []
        for i in range (0,3):
            for j in range (0,3):
                if board[i][j] == None: 
                    moves.append({"row": i, "col":j})
        for move in moves: 
            board[move['row']][move['col']] = "O"
            if minimax(board, "X")[0] > value: 
                value = minimax(board, "X")[0]
                bestmove = move
            board[move['row']][move['col']] = None
    return (value, bestmove)