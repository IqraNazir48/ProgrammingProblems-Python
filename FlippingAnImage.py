
def flipAndInvertImage(image):
    """
    :type image: List[List[int]]
    :rtype: List[List[int]]
    """
    image2=[]
    
    for i in range(len(image)):
        l=[]
        for j in range(len(image[i])-1,-1,-1):
            l.append(image[i][j])
        image2.append(l)
    
    for i in range(len(image)):
        for j in range(len(image[i])):
            if(image2[i][j]==0):
                image2[i][j]=1
            else:
                image2[i][j]=0
    return image2


image =[[1,1,0],[1,0,1],[0,0,0]]
print(f"Before: {image}")
result=flipAndInvertImage(image)
print(f"After: {result}")



