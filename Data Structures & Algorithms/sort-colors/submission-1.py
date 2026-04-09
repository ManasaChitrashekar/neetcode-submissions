class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #In the Dutch National Flag algorithm, when you swap the current element with the right boundary (for value 2), 
        #you must not increment the current pointer. The swapped element from the right has not been examined yet and could be 0, 1, or 2.
        l,m,r = 0 , 0,len(nums)-1
        while m<=r:
            if nums[m]==0:
                nums[l],nums[m]=0,nums[l]
                l +=1
                m +=1
            elif nums[m]==1:
                m +=1
            elif nums[m]==2:
                nums[r],nums[m]=2,nums[r]
                r -=1

        