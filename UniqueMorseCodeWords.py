
def uniqueMorseRepresentations( words):
    """
    :type words: List[str]
    :rtype: int
    """
    dictionary={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",
            'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",
            'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",
            'q':"--.-",
            'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",
            'w':".--",'x':"-..-",'y':"-.--",'z':"--.."
            }
    l=[]
    for i in range(len(words)):
        string=""
        for j in range(len(words[i])):
            string=string+(dictionary[words[i][j]])
        l.append(string)
    return len( set(l))

words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresentations(words))
words = ["a"]
print(uniqueMorseRepresentations(words))