class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #the traditional top-down approach will have duplicates
        #to avoid duplicates, we will not reuse the numbers
        res, sol = [],[]
        n = len(nums)
        def backtrack(i, cur_sum):
            if cur_sum ==  target:
                res.append(sol[:])
                return
            if i >= n or cur_sum >target:
                return
            #branch out
            #dont take the current index
            backtrack(i+1, cur_sum)
            #take the current index
            sol.append(nums[i])
            backtrack(i,cur_sum+nums[i])
            sol.pop()
        backtrack(0,0)
        return res

        