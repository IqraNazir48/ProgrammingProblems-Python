def largestGoodInteger( num):
    num=list(num)
    l=[]
    count=0;
    for i in range(1,len(num)):
        if(num[i]==num[i-1]):
            count+=1
            if(count==2):
                l.append(num[i])
        else:
            count=0
    if(len(l)==0):
        return ""
    largest=max(l)
    string=""+largest+largest+largest
    return string
l="33767666"
print(largestGoodInteger(l));