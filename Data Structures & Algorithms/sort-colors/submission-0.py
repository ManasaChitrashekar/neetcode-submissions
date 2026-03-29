class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        two = len(nums)-1
        i = 0 
        while i<=two:
            if nums[i]==0:
                tmp = nums[zero]
                nums[zero]= 0 
                nums[i]=tmp
                zero +=1
            elif nums[i]==2:
                tmp = nums[two]
                nums[two]=  2
                nums[i]=tmp
                two -=1
                i -=1
            i +=1
        

               
        """
        Do not return anything, modify nums in-place instead.
        """
        