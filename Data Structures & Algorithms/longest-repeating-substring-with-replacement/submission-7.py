class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left,max_result = 0,0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            current_max = max(count.values())
            current_len = right-left+1
            if current_len - current_max > k:
                #we are in invalid range
                count[s[left]]-=1
                left+=1
            max_result = max(max_result,right-left+1)
        return max_result

        