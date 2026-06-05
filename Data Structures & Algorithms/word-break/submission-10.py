class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        #wordSet = set(wordDict)
        return self.helper(s,wordDict,memo)
    def helper(self,s,wordSet,memo):
        if s in memo: return memo[s]
        if s == "": return True
        #branch out
        for word in wordSet:
            if word in s and s.index(word) == 0:
                rem = s[len(word):]
                if self.helper(rem,wordSet,memo):
                    memo[s] = True
                    return True
        memo[s] =  False
        return False
        
        