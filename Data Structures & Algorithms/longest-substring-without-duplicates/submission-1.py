class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       # we can leverage a sliding window
       # the window would continue to increase as long as the chars are not
       # seen earlier
       # if the character is seen, continue to remove chars starting from the
       # left side 
       # calculate the max size r-l+1 in every iteration
       # return the max window size
       max_window_size,seen = 0, set()
       left = 0
       for right, c in enumerate(s):
        while c in seen:
            seen.remove(s[left])
            left+=1
        seen.add(c)
        max_window_size = max(max_window_size,right-left+1)
       return max_window_size
       
    
    
        