class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(pos,num_arr,memo={}):
            if pos in memo: return memo[pos]
            if pos>=len(nums):
                return 0
            memo[pos] = max(helper(pos+1,nums),nums[pos]+helper(pos+2,nums)) 
            return memo[pos]
        return helper(0,nums)