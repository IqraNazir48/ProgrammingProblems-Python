def list_to_number(list1):
    n=1
    for i in range(len(list1)-1):
        n*=10
    number=0
    for i in range(len(list1)):
        number=number+list1[i]*n;
        n/=10
    return int(number)
def maximum69Number ( num):
    """
    :type num: int
    :rtype: int
    """
    list1=list((str(num)))
    for i in range(len(list1)):
        list1[i]=int(list1[i])
    list2=[num]
    for i in range(len(list1)):
        list3=list(list1)
        if(list3[i]==6):
            list3[i]=9
        else:
            list3[i]=6
        list3=list_to_number(list3)
        list2.append(list3)
    return max(list2)
    
number=int(input("Ente the number : "))
print(maximum69Number(number))