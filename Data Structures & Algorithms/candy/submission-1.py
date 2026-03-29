class Solution:
    def candy(self, ratings: List[int]) -> int:
         nums = ratings
         res = [1]*len(nums)
    #1st pass:
         for i in range(1,len(nums)):
            if nums[i] > nums[i-1] :
                res[i] = res[i-1]+1
    #2pass
         for i in range(len(nums)-2,-1,-1):
            if  nums[i]>nums[i+1]:
                res[i] = max(res[i],res[i+1]+1)
         return sum(res)