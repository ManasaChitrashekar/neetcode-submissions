class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,h = max(nums),sum(nums)
        while l < h :
            mid = (l+h)//2
            subarray = 1
            cursum = 0
            for num in nums:
                cursum += num
                if cursum > mid:
                    subarray +=1
                    cursum = num
            if subarray > k:
                l = mid +1
            else :
                h = mid 
        return l 
