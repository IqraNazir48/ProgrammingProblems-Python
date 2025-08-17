def rotateString( s, goal):
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    if(len(s)!=len(goal)):
        return False
    for i in range(0,len(s)):
        if(s==goal):
            return True
        char1=s[0]
        s=str(s[1:len(s)]+char1)

    return False


s ="abcde"
goal ="cdeab"
print(rotateString(s,goal))