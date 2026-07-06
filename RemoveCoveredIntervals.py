def isCovered(in1, in2):
    if(in2[0]<=in1[0] and in1[1]<=in2[1]):
        return True
    
def removeCoveredIntervals(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        count=0
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if(isCovered(intervals[i],intervals[j]) and intervals[i][0]!=-1 and intervals[i][1]!=-1 and i!=j):
                    intervals[i][0]=-1
                    intervals[i][1]=-1
                    count+=1
                    break
        return (len(intervals))-count
        

intervals = [[1,4],[3,6],[2,8]]   # 2
print(removeCoveredIntervals(intervals))