def repeatedNTimes_solution_01( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count=len(nums)/2
    dic={}
    for i in range(len(nums)):
        if(nums[i] not in dic):
            dic[nums[i]]=1
        else:
            dic[nums[i]]=dic[nums[i]]+1
    
    l=list(dic.keys())
    for i in range(len(dic)):
        if(dic[l[i]]==count):
            return l[i]
        
def repeatedNTimes_solution_02( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count=len(nums)/2
    s=list(set(nums))
    for i in range(len(s)):
        if(nums.count(s[i])==count):
            return s[i]
    

nums = [1,2,3,3] # 3
print(repeatedNTimes_solution_01(nums))
print(repeatedNTimes_solution_02(nums))

nums = [2,1,2,5,3,2] #2
print(repeatedNTimes_solution_01(nums))
print(repeatedNTimes_solution_02(nums))

nums = [5,1,5,2,5,3,5,4]# 5
print(repeatedNTimes_solution_01(nums))
print(repeatedNTimes_solution_02(nums))

