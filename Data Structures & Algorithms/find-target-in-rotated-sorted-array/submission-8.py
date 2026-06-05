class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            # search right
            if nums[mid] == target:
                 return mid
            if nums[mid] >= nums[left]:
                if nums[mid] < target or target < nums[left]:
                    #go right
                    left = mid+1
                else:
                    right = mid-1
            else:
                #we are on the right side
                if nums[mid] > target or target > nums[right]:
                    #go left
                    right  = mid-1
                else:
                    left = mid+1
        return -1
            
        