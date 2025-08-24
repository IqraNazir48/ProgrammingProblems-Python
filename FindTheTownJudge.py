
def findJudge( n, trust):
    """
    :type n: int
    :type trust: List[List[int]]
    :rtype: int
    """
    if(len(trust)==0 and n==1):
        return 1
    l=[]
    for i in range(len(trust)):
        if(trust[i][0] not in l):
            l.append(trust[i][0])
        if(trust[i][1] not in l):
            l.append(trust[i][1])

    c=len(l)-1
    for i in range(len(l)):
        count=0
        flag=0
        for j in range(len(trust)):
            if(trust[j][0]==l[i]):
                flag=1
            elif(trust[j][1]==l[i]):
                count+=1
        if(count==c and flag==0):
            return l[i]
    return -1
    

people1=2
trust1 = [[1,2]]
print(f"Town Judge in Town 1  : {findJudge(people1,trust1)} ")

people2= 3
trust2 = [[1,3],[2,3],[3,1]]
print(f"Town Judge in Town 2 : {findJudge(people2,trust2)} ")
