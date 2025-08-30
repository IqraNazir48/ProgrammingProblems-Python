def isvalid(l):
    if(len(l)==len(set(l))):
        return True
    return False
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    #rows check
    for i in range(9):
        l=[]
        for j in range(9):
            if(board[i][j]!="."):
                l.append(int(board[i][j]))
        if(isvalid(l)==False):
            return False
    print("Passed in row check")
    #column check
    for i in range(9):
        l=[]
        for j in range(9):
            if(board[j][i]!="."):
                l.append(int(board[j][i]))
        if(isvalid(l)==False):
           return False
    print("Passed in column check")
    #1st three boxes
    l1=[]
    l2=[]
    l3=[]
    for i in range(3):
        for j in range(9):
            if(j<3 and board[i][j]!="."):
                l1.append(int(board[i][j]))
            elif(j>=3 and j<6 and board[i][j]!="."):
                l2.append(int(board[i][j]))
            elif(j>=6 and board[i][j]!="."):
                l3.append(int(board[i][j]))

    if(isvalid(l1)==False or isvalid(l2)==False or isvalid(l3)==False):
        return False
    
    print("1st three boxes passed")
    l1=[]
    l2=[]
    l3=[]
    #next 3 boxes
    for i in range(3,6):
        for j in range(9):
            if(j<3 and board[i][j]!="."):
                l1.append(int(board[i][j]))
            elif(j>=3 and j<6 and board[i][j]!="."):
                l2.append(int(board[i][j]))
            elif(j>=6 and board[i][j]!="."):
                l3.append(int(board[i][j]))

    if(isvalid(l1)==False or isvalid(l2)==False or isvalid(l3)==False):
        return False
    #last 3 boxes
    l1=[]
    l2=[]
    l3=[]
    for i in range(6,9):
        for j in range(9):
            if(j<3 and board[i][j]!="."):
                l1.append(int(board[i][j]))
            elif(j>=3 and j<6 and board[i][j]!="."):
                l2.append(int(board[i][j]))
            elif(j>=6 and board[i][j]!="."):
                l3.append(int(board[i][j]))

    if(isvalid(l1)==False or isvalid(l2)==False or isvalid(l3)==False):
        return False
    print("last three boxes passed")
    return True

board=[[".",".",".","3",".",".",".","1","."],
       [".",".",".",".",".","7",".",".","."],
       [".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".","8","2","7","."],
       ["1",".",".",".",".",".",".",".","."],
       [".",".",".","5",".",".",".",".","."],
       ["2",".",".",".","8",".",".",".","7"],
       ["7",".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."]]

print(isValidSudoku(board))