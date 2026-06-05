from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        st = deque()
        for i,temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                poped_index = st.pop()
                result[poped_index] = i-poped_index
            st.append(i)
            

        return result
        