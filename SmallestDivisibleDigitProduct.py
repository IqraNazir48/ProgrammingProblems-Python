def product_of_digits( n):
    integer=str(n)
    number=1
    for i in range(len(integer)):
        number=number*int(integer[i])
    return number
def smallestNumber(n, t):
    """
    :type n: int
    :type t: int
    :rtype: int
    """
    while(product_of_digits(n)%t!=0):
        n=n+1
    return n


n=10 
t=2
print(smallestNumber(n,t))

n=15
t=3
print(smallestNumber(n,t))