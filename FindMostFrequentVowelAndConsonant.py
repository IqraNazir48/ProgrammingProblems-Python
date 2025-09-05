def maxFreqSum(s):
    """
    :type s: str
    :rtype: int
    """
    vowels=[0]
    consonants=[0]
    string=list(set(list(s)))
    v=['a','e','i','o','u']
    for i in range(len(string)):
        if(string[i] not in v):
            vowels.append(s.count(string[i]))
        else:
            consonants.append(s.count(string[i]))
    return max(vowels)+max(consonants)


s = "aeiaeia" # 3
print(maxFreqSum(s))

s = "successes" # 6
print(maxFreqSum(s))
