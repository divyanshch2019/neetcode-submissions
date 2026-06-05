class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                #either I am going to append left
                res.append(newInterval)
                #we can return from here
                return res + intervals[i:]
            elif intervals[i][1]<newInterval[0]:
                #or right
                res.append(intervals[i])
            else:
                 #or merge
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res

        
       
        