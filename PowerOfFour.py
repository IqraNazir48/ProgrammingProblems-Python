def isPowerOfFour(n):
        if(n<=0):
            return False
        power=1
        for i in range(30):
            if(n==power):
                return True
            power=power*4
        return False

n=int(input("Enter the Number: "))
if(isPowerOfFour(n)):
    print(f"{n} is power of Four.")
else:
    print(f"{n} is not power of Four.")