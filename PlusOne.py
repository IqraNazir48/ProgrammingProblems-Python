def plusOne( digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    n=len(digits)-1
    val=1
    for i in range(n):
        val=val*10
    temp=val
    num=0
    for i in digits:
        num=num+(i*val)
        val=int(val/10)
    num=num+1
    l=list(str(num))
    result=[]
    for i in l:
        result.append(int(i))
    return result

digits = [1,2,3]
print(plusOne(digits))
        