def countBalls(lowLimit, highLimit):
    """
    :type lowLimit: int
    :type highLimit: int
    :rtype: int
    """
    l={}
    for i in range(lowLimit,highLimit+1):
        string=str(i)
        s=0
        for j in range(len(string)):
            s=s+(int(string[j]))
        if(l.get(str(s))==None):
            l[str(s)]=1
        else:
            l[str(s)]=l[str(s)]+1
        
    result=l.values()
    return max(result)

lowerLimit=22
highLimit=45
print(f"Maximum Number Of Balls In A Box : {countBalls(lowerLimit,highLimit)}")