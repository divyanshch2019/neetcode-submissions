class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_result,prefix = [1]*n,1
        for i in range(1,n):
            left_result[i] = nums[i-1]*prefix
            prefix=left_result[i]
        right_result = [1]*n
        prefix = 1
        for i in range(n-2,-1,-1):
            right_result[i] = prefix*nums[i+1]
            prefix = right_result[i]
        result = []
        for i in range(n):
            result.append(left_result[i]*right_result[i])
        return result

