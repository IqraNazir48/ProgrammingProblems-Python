def fib(n):
    """
    :type n: int
    :rtype: int
    """
    first=0
    second=1
    if(n==0):
        return 0
    if(n==1):
        return 1
    for i in range(n-1):
        value=first+second
        first=second
        second=value
    return second

print("For n=0, the Fibonacci number is: ", fib(0))
print("For n=1, the Fibonacci number is: ", fib(1))
print("For n=2, the Fibonacci number is: ", fib(2))                 
print("For n=3, the Fibonacci number is: ", fib(3))
print("For n=4, the Fibonacci number is: ", fib(4))
print("For n=5, the Fibonacci number is: ", fib(5))