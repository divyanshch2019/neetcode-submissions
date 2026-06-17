class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #store the numbers in the set
        #find the starting points
        #loop over the available starting points and keep incrementing as long as the number+1
        #exist
        num_set = set(nums)
        starting_points,result =[],0
        for n in nums:
            if n-1 not in num_set: 
                temp_result = 0
                current =n
                while current in num_set:
                    temp_result+=1
                    current+=1
                result = max(result,temp_result)
           
        return result

