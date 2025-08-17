def findRestaurant( list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    minimum=99999999
    result=[]
    for i in range(0,len(list1)):
        if(list1[i] in list2):
            j=list2.index(list1[i])
            if(i+j<minimum):
                result=list([])
                minimum=i+j
                result.append(list1[i])
            elif(i+j==minimum):
                minimum=i+j
                result.append(list1[i])


    return result
    



list1 =["Shogun","Piatti","Tapioca Express","Burger King","KFC"]
list2 =["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

print(findRestaurant(list1,list2))
