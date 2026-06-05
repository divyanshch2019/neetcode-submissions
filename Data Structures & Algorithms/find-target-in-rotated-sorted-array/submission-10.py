class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            # search right
            if nums[mid] == target:
                 return mid
            #left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left]<=target <nums[mid]:
                    #search left
                    right = mid-1
                else:
                    left = mid+1
            else:
                #we are on the right side
                if nums[mid] > target or target > nums[right]:
                    #go left
                    right  = mid-1
                else:
                    left = mid+1
        return -1
            
        