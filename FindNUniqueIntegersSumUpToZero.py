def sumZero( n):
    """
    :type n: int
    :rtype: List[int]
    """
    result=[]
    if(n%2==0):
        size=int(n/2)
    else:
        size=int((n-1)/2)
        result.append(0)

    for i in range(1,size+1):
        result.append(i)
        result.append(-1*i)
    
    return result


n=5
print(sumZero(n))

n=3
print(sumZero(n))

n=1
print(sumZero(n))