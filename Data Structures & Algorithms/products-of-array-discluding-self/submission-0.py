class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result =[]
        n = len(nums)
        left,right = [1]*n,[1]*n

        #cal product of all the elements to the left of current
        prev_prod = 1
        for i in range(1,n):
            prev_prod = prev_prod * nums[i-1]
            left[i] = prev_prod
        #cal prod of all the elements to the right of the current
        prev_prod = 1
        for i in range(n-2,-1,-1):
            prev_prod = prev_prod * nums[i+1]
            right[i] = prev_prod
        for i in range(n):
            result.append(left[i]*right[i])
        return result



        