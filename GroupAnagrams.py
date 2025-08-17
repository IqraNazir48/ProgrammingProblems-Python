
def sorted_strings(strs):
    for i in range(len(strs)):
        string=list(strs[i])
        string.sort()
        string="".join(string)
        strs[i]=string
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    done={0}
    strings=list(strs)
    sorted_strings(strings)
    result=[]
    for i in range(len(strs)):
        if(strs[i] in done):
            continue
        string=strings[i]
        l=[]
        l.append(strs[i])
        done.add(strs[i])
        for j in range(i+1,len(strs)):
            if(strings[j]==string):
                l.append(strs[j])
                done.add(strs[j])
        result.append(l)
    return result


strs=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
