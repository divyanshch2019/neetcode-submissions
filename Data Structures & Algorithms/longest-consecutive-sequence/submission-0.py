class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #check if the current num -1 is in the list
        #if yes, then skip the number because the current number
        #is already part of a sequence
        #else, consider the current as the start of a loop
        #increamnet the size by one when we find the current+1 in the
        #list
        #to reduce the time search time, add all the nums to a hash set
        nums_set = set(nums)
        result = 0
        for num in nums:
            if num-1 in nums_set: continue
            temp,current = 0,num
            while current in nums_set:
                temp+=1
                current+=1
            #update max sequence length
            result = max(result,temp)

        return result
        