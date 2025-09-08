def containsZero(n):
    n=str(n)
    l=list(n)
    for i in range(len(l)):
        if(l[i]=='0'):
            return False
        
    return True
    
def getNoZeroIntegers( n):
    """
    :type n: int
    :rtype: List[int]
    """
    i=1
    j=n-1
    for k in range(n):
        if(i+j==n and containsZero(i)==True and containsZero(j)==True):
            return [i,j]
        i=i+1
        j=j-1


n=534
print(getNoZeroIntegers(n))

