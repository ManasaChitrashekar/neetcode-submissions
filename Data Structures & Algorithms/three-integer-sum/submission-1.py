class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)-1
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            l=i+1
            r=n
            while(l<r):
                s = nums[i]+nums[l]+nums[r]
                if s>0 :
                    r-=1
                if s<0:
                    l+=1
                elif s==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while (l <r and nums[l-1]==nums[l]):
                        l+=1
                    while (l <r and nums[r]==nums[r+1]):
                        r-=1
        return res    
