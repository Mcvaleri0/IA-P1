import math

def board_perform_move(board, move):
    temp = []
    for line in board:                  #cause python doesn't uses references 
        temp += [line.copy()]

    before = move[0]
    after = move[1]
    mid = (int(math.fabs(after[0]-before[0])//2), int(math.fabs(after[1]-before[1])//2))
    print(mid)
    temp[before[0]][before[1]] = "_"
    temp[after[0]][after[1]] = "O"
    temp[mid[0]][mid[1]] = "_"
    return temp