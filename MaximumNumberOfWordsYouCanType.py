def canBeTypedWords( text, brokenLetters):
    """
    :type text: str
    :type brokenLetters: str
    :rtype: int
    """
    l=text.split(" ")
    count=0
    for i in range(len(l)):
        flag=0
        for j in range(len(l[i])):
            if(l[i][j] in brokenLetters):
                flag=1
                break
        if(flag==0):
            count+=1

    return count


text = "leet code"
brokenLetters = "lt"
print(canBeTypedWords(text,brokenLetters))

text = "leet code"
brokenLetters = "e"
print(canBeTypedWords(text,brokenLetters))
