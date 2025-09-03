# Input: s = "IceCreAm"

# Output: "AceCreIm"
def reverseVowels( s):
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
    l.reverse()
    result=""
    for i in range(len(s)):
        if(s[i] in vowels):
            result+=str(l[j])
            j=j+1
        else:
            result+=s[i]
    return result

s = "IceCreAm"
print(reverseVowels(s))