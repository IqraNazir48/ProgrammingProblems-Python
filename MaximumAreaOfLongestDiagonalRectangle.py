import math
def areaOfMaxDiagonal(dimensions):
    """
    :type dimensions: List[List[int]]
    :rtype: int
    """

    maximum=0
    diagonal=[]
    selectedIndex=[]
    for i in range(len(dimensions)):
        n1=dimensions[i][0]
        n2=dimensions[i][1]
        p=(n1*n1)+(n2*n2)
        val=math.sqrt(p)
        if(val>maximum):
            maximum=val
            selectedIndex=i
        diagonal.append(val)
    indices=[]
    for i in range(len(diagonal)):
        if(diagonal[i]==maximum):
            indices.append(i)
    result=0
    for i in range(len(indices)):
        v=dimensions[indices[i]][0]*dimensions[indices[i]][1]
        if(v>result):
            result=v
    return result




dimensions = [[9,3],[8,6]]
print(areaOfMaxDiagonal(dimensions))

