class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since the given array is sorted we can use 2-ptr to find the target result
        left,right = 0,len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right] < target:
                #move right
                left+=1
            elif numbers[left]+numbers[right] > target:
                #reduce the overall sum, move right
                right-=1
            else:
                return [left+1,right+1]
        return []
        