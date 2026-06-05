class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            cur = intervals[i]
            #merge left
            if newInterval[1] < cur[0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif cur[1] < newInterval[0]:
                result.append(cur)
            else:
                #merge
                newInterval = [min(cur[0],newInterval[0]),max(cur[1],newInterval[1])]
        result.append(newInterval)
        return result
        