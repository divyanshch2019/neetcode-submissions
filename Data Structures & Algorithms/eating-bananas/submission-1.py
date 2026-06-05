class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,sum(piles)
        def feasible(k):
            result = 0
            for p in piles:
                result+=math.ceil(p/k)
            return result <=h
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid+1
        return left
        