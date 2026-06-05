class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res, prevEnd = 0, intervals[0][1]
        for i in range(1,len(intervals)):
            start,end = intervals[i]
            if start>=prevEnd:
                #update the prevEnd
                prevEnd = end
            else:
                #overlap detected
                res+=1
                prevEnd = min(prevEnd,end)
        return res
        