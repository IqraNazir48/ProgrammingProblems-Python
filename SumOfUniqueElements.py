def sumOfUnique(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if(len(nums)==1):
        return nums[0]
    nums.sort()
    count=1
    result=0
    i=0
    for i in range(1,len(nums)):
        if(nums[i]!=nums[i-1]):
            if(count==1):
                result=result+nums[i-1]
            count=1
        else:
            count=count+1
    if(nums[i]!=nums[i-1]):
        result=result+nums[i]
    return result

nums=[1,2,3,3,4,5]

print(f"The sum of Unique elements in nums  : {sumOfUnique(nums)}")