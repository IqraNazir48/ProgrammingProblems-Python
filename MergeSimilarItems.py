def mergeSimilarItems( items1, items2):
    """
    :type items1: List[List[int]]
    :type items2: List[List[int]]
    :rtype: List[List[int]]
    """
    values2=[]
    weight2=[]
    for i in range(len(items2)):
        values2.append(items2[i][0])
        weight2.append(items2[i][1])
    
    result=[]
    for i in range(len(items1)):
        if(items1[i][0] in values2):
            index=int(values2.index(items1[i][0]))
            list=[]
            list.append(items1[i][0])
            list.append(items2[index][1]+items1[i][1])
            result.append(list)
            items2[index]=[0,0]
        else:
            result.append(items1[i])
    for i in range(len(items2)):
        if(items2[i]!=[0,0]):
            result.append(items2[i])
    result.sort(key=lambda x: x[0])
    return result






items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
# Output: [[1,6],[3,9],[4,5]]
print(mergeSimilarItems(items1,items2))

items1 = [[1,3],[2,2]]
items2 = [[7,1],[2,2],[1,4]]
# Output: [[1,7],[2,4],[7,1]]
print(mergeSimilarItems(items1,items2))
    