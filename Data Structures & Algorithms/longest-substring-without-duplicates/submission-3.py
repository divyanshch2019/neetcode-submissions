class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        longest_result = 1
        if len(s)<2: return longest_result
        seen = {}
        start = 0
        for end in range(len(s)):
            while s[end] in seen and start<=seen[s[end]]:
                start = seen[s[end]]+1
                del seen[s[end]]
            
            #add current element to seen, update the max result
            seen[s[end]]=end
            longest_result = max(longest_result, end-start+1)
                
        
        return longest_result
        