class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the intervals
        res = []
        intervals.sort(key=lambda x:x[0])
        newInterval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= newInterval[1]:
                #overlapping intervals
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
                continue
            #then add the current interval to the result
            res.append(newInterval)
            #res.append(intervals[i])
            newInterval = intervals[i]
        res.append(newInterval)
        return res
        

        