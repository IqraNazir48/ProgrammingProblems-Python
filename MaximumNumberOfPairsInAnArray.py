def numberOfPairs(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    for i in range(1,len(nums)):
        if(nums[i]==nums[i-1]):
            nums[i]=-100
            nums[i-1]=-100
    count1=0
    count2=0
    for i in range(len(nums)):
        if(nums[i]==-100):
            count1=count1+1
        else:
            count2=count2+1

    result=[int((count1)/2),count2]
    return result


nums = [1,3,2,1,3,2,2]
print(numberOfPairs(nums))