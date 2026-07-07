def sumAndMultiply(n):
    """
    :type n: int
    :rtype: int
    """
    if(n==0):
        return 0
    string=str(n)
    sum=0
    result=''
    for i in range(len(string)):
        if(int(string[i])!=0):
            sum+=int(string[i])
            result+=string[i]
    return int(result)*sum

print(sumAndMultiply(10203004))
        