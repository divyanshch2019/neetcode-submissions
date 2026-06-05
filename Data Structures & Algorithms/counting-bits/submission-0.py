class Solution:
    def countOne(self,num):
        count = 0
        while num:
            num&=num-1
            count+=1
        return count
    def countBits(self, n: int) -> List[int]:
        return [self.countOne(i) for i in range(n+1)]
        