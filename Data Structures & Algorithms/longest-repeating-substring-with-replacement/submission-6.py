class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count,result = {},0
        def mostFrequentCount():
           return max(count.values())
        left = 0
        for right,c in enumerate(s):
            #add current to the count
            count[c] = 1 + count.get(c,0)
            
            #check if the current chars to be substituted is less than the k
            if right-left+1 - mostFrequentCount()>k:
                count[s[left]]-=1
                left+=1
            result = max(result, right-left+1)
        return result
           

        