class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort the interval based on the start value
        intervals.sort()
        res = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            current = intervals[i]
            #they will overlap if the current_start < prev_end
            if current[0] < prev[1]:
                res+=1
                #remove the whose end is greater
                if current[1] < prev[1]:
                    prev = current
            else:
                prev = current


        return res
        