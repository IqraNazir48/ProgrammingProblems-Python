def intersect( nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    l=[]
    for i in range(len(nums1)):
        if(nums1[i] in nums2):
            l.append(nums1[i])
            nums2.remove(nums1[i])
    return l
    

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersect(nums1,nums2))