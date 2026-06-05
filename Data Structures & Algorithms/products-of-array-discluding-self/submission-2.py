class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        #find the left product
        for i in range(1,n):
            result[i] = result[i-1]*nums[i-1]
        rightProduct =1
        for j in range(n-2,-1,-1):
            rightProduct*=nums[j+1]
            result[j] *=rightProduct
        return result

        