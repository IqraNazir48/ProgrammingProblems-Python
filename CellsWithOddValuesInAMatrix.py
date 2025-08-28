def oddCells( m, n, indices):
    """
    :type m: int
    :type n: int
    :type indices: List[List[int]]
    :rtype: int
    """
    matrix=[]
    for i in range(m):
        arr=[]
        for j in range(n):
            arr.append(0)
        matrix.append(arr)
    for i in range(len(indices)):
        row=indices[i][0]
        column=indices[i][1]
        for j in range(n):
            matrix[row][j]=matrix[row][j]+1
        for k in range(m):
            matrix[k][column]=matrix[k][column]+1
        
    odds=0
    for i in range(m):
        for j in range(n):
            if(matrix[i][j]%2!=0):
                odds+=1
    return odds


m = 2
n = 3
indices = [[0,1],[1,1]]
print(oddCells(m,n,indices))


m = 2
n = 2
indices = [[1,1],[0,0]]
print(oddCells(m,n,indices))

