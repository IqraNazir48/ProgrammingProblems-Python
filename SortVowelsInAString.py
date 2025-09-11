# Input: s = "IceCreAm"

# Output: "AceCreIm"
def sorting(l):
    result=[]
    for i in range(len(l)):
        result.append(ord(l[i]))
    
    return result


def sortVowels( s):
    """
    :type s: str
    :rtype: str
    """
    vowels=['a','e','i','o','u','A','E','I','O','U']
    l=[]
    for i in range(len(s)):
        if(s[i] in vowels):
            l.append(s[i])
    j=0
    sorted=sorting(l)
    sorted.sort()
    result=""
    for i in range(len(s)):
        if(s[i] in vowels):
            result+=(chr(sorted[j]))
            j=j+1
        else:
            result+=s[i]
    return result

s = "IceCreAm"
s = "lEetcOde"
# Output: "lEOtcede"
print(sortVowels(s))