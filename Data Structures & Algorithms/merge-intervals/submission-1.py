class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        #sort the incoming interval array
        intervals.sort(key= lambda x:x[0])
        prev_start,prev_end = intervals[0]
        for i in range(1,len(intervals)):
            current_start,current_end = intervals[i]
            if current_start <= prev_end:
                #prev and current intervals merge
                prev_end = max(prev_end,current_end)
                continue
            #if you are here, then push the prev data to the output and assign the current 
            # to the prev
            result.append([prev_start,prev_end])
            prev_start,prev_end = intervals[i]
        # push last data
        result.append([prev_start,prev_end])
        return result
            