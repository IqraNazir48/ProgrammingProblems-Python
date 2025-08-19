
def zeroFilledSubarray( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    consecutive_zeros=[]
    count=0
    for i in range(len(nums)):
        if(nums[i]==0):
            consecutive_zeros.append(count)
            count=count+1
        else:
            consecutive_zeros.append(count)
            count=0
    if(nums[len(nums)-1]==0):
        consecutive_zeros.append(count)
    result=0
    for i in range(len(consecutive_zeros)):
        result+=consecutive_zeros[i]
    return result

nums=[0,0,0,2,0,0]
print(f"The number of zero filled subarrays in nums : {zeroFilledSubarray(nums)}")