
def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    result=[]
    for i in range(len(nums1)-1):
        index=nums2.index(nums1[i])
        flag=0
        for j in range(index+1,len(nums2)):
            if(nums2[j]>nums1[i]):
                result.append(nums2[j])
                flag=1
                break
        if(flag==0):
            result.append(-1)


    result.append(-1)
    return result
        



nums1 = [4,1,2]
nums2 = [1,3,4,2]
# Output: [-1,3,-1]
print(nextGreaterElement(nums1,nums2))


nums1 = [2,4]
nums2 = [1,2,3,4]
# Output: [3,-1]
print(nextGreaterElement(nums1,nums2))

