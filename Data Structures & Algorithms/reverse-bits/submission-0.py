class Solution:
    def reverseBits(self, n: int) -> int:
        #read lsb
        #push it to msb and keep move
        res = 0
        for i in range(32):
            lsb = (n>>i)&1
            mask = lsb<<(31-i)
            res+=mask
        return res
        