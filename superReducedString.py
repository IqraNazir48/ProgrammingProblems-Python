def superReducedString(s):
    # Write your code here
    s=list(s)
    flag=1
    i=0
    while(flag==1):
        flag=0
        for i in range(len(s)-1):
            if(s[i]==s[i+1]):
                s.pop(i)
                s.pop(i)
                flag=1
                break
    result=''
    for i in range(len(s)):
        result+=s[i]
    return result

# aaabccddd
# aaabccddd → abccddd → abddd → abd
print(superReducedString('aaabccddd'))
# aa
# aa → Empty String

print(superReducedString('aa'))
# baab
# baab → bb → Empty String
print(superReducedString('baab'))