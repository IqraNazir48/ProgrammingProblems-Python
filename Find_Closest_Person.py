
def findClosest( x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: int
    """
    
    x_distance=abs(z-x)
    y_distance=abs(z-y)

    if(x_distance==y_distance):
        return 0
    elif ( x_distance<y_distance):
        return 1
    else:
        return 2


x = 2
y = 7
z = 4#1
print(findClosest(x,y,z))


x = 1
y = 5
z = 3#0
print(findClosest(x,y,z))

x = 2
y = 5
z = 6#2

print(findClosest(x,y,z))