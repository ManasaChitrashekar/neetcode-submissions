class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findfirst(nums,target):
            l,h = 0, len(nums)-1
            res = -1
            while l <=h :
                mid = l+(h-l)//2
                if nums[mid]==target:
                    res= mid 
                    h = mid-1
                elif nums[mid]<target:
                    l = mid+1
                else:
                    h = mid-1
            return res
        def findlast(nums,target):
            l,h = 0, len(nums)-1
            res = -1
            while l <=h :
                mid = l+(h-l)//2
                if nums[mid]==target:
                    res= mid 
                    l = mid+1
                elif nums[mid]<target:
                    l = mid+1
                else:
                    h = mid-1
            return res
        low = findfirst(nums,target)
        high = findlast(nums,target) 
        return [low,high]