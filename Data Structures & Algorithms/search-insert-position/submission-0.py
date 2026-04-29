class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            mid = l + ((h-l)//2)
            if target==nums[mid]:
                return mid
            if target<nums[mid]:
                h = mid-1
            else:
                l = mid+1
        return l