class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if target ==nums[mid]: return mid
            #find which side is sorted
            if nums[left]<=nums[mid]:
                #if target falls with in the bound of left and mid, then search left else right
                if nums[left]<=target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                #right side is sorted
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1

        