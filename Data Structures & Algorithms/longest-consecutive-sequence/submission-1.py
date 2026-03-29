class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in numset:
            if num-1 not in numset:
                count = 0
                while num+count in numset:
                    count +=1
                res = max(res,count)
        return res
