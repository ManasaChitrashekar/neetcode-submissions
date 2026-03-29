class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)-1
        rowlen = len(matrix[0])-1
        while(low<=high):
            midrow = low+(high-low)//2
            if(target<matrix[midrow][0]):
                high=midrow-1
            elif(target>matrix[midrow][rowlen]):
                low=midrow+1
            else:
                return self.bs(matrix[midrow],target)    
        return False
    def bs(self,nums,target:int)->bool:
        low,high = 0,len(nums)-1
        while(low<=high):
            mid = low+(high-low)//2
            if(target==nums[mid]):
                return True
            elif(target<nums[mid]):
                high = mid-1
            else :
                low = mid+1    
        return False    