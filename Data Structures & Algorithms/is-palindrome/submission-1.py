class Solution:
    def isPalindrome(self, s: str) -> bool:
        #keep check the pointers from start and end and move inwards
        #discard invalid chars by checking if they are not alnum
        #if any comparison fail, return false otherwise continue to move inwards
        left, right =0,len(s)-1
        while left < right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            #valid input char, run the core algo
            if s[left].lower()!=s[right].lower(): return False
            left+=1
            right-=1
        return True
        