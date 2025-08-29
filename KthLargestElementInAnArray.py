def findKthLargest( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    
    
    nums.sort()
    index=len(nums)-k
    return nums[index]

nums = [3,2,1,5,6,4]
k = 2
print(f"Kth largest element in array is : {findKthLargest(nums,k)}")

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(f"Kth largest element in array is : {findKthLargest(nums,k)}")
