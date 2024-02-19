#Chess Dictionary Validator
board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard():


    pieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
    colors = ['w', 'b']
    y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x = ['1', '2', '3', '4', '5', '6', '7', '8']
    bpieces, wpieces = 0, 0
    bking, wking, bpawn, wpawn = 0, 0, 0, 0

    if 'bking' in board.values():
        bking += 1
    if 'wking' in board.values():
        wking += 1
    if 'bpawn' in board.values():
        bpawn += 1
    if 'wpawn' in board.values():
        wpawn += 1
    print(bking, wking, bpawn, wpawn)

    #count the number of black and white pieces
    for piece in board.values():
        if piece[0] == 'b':
            bpieces += 1
        elif piece[0] == 'w':
            wpieces += 1
    print(bpieces, wpieces)
    
    #one black king and one white king
    
    if bking and wking != 1:
        return False
    
    #each player can have at most 16 pieces
    if bpieces or wpieces > 16:
        return False
    #no more than 8 pawns
    if bpawn or wpawn > 8:
        return False
    #all pieces must be on a valid space from '1a' to '8h'
    for pos in board.keys():
        if pos[0] not in x or pos[1] not in y:
            return False
            
    #pieces begin with either 'w' or 'b' followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
    for piece in board.values():
        if piece[0] not in colors or piece[1:] not in pieces:
            return False    
    #should detect when a bug has resulted in an improper chess board state
    else :
        return True
print(isValidChessBoard())