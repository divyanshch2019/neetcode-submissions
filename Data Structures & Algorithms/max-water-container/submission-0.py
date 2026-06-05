class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0,len(heights)-1
        max_result = 0
        while left<right:
            temp_area = min(heights[left],heights[right])*(right-left)
            max_result = max(max_result,temp_area)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return max_result
        