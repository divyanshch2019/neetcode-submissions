class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =len(nums)
        product_result = [1]*n
        for i in range(1,n):
            #left product
            product_result[i] = product_result[i-1]*nums[i-1]
        right = 1
        for j in range(n-2,-1,-1):
            right*=nums[j+1]
            product_result[j] *=right

        return product_result        