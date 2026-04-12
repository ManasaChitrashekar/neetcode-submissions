class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,h = 0,len(nums)-1

        while l < h:
            mid = l+(h-l)//2
            #if mid is greated than value next to it it mens its in downsterat so either mid is peak or we find 
            #better peak moving right to mid 
            if nums[mid]>nums[mid+1]:
                h = mid
            else:
                l = mid +1
        return h