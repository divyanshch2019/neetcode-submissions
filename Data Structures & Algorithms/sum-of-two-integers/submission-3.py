class Solution:
    def getSum(self, a: int, b: int) -> int:
        # to handle only the first 32 bits, we would use a mask
        mask= 0xffffffff
        while (b&mask) >0:
            carry = (a&b)<<1
            a = a ^b
            b = carry
        return (a&mask) if b>0 else a
        