class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        h = len(matrix)-1
        rows,cols = len(matrix),len(matrix[0])
        def search(nums) :
            l=0
            h=len(nums)-1
            while l<=h:
                mid = l + ((h-l)//2)
                if target==nums[mid]:
                    return True
                if target<nums[mid]:
                    h = mid-1
                else:
                    l = mid+1
            return False
        
        while l<=h:
            mid = l + ((h-l)//2)
            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
               return search(matrix[mid])
            elif target< matrix[mid][0]:
                h = mid-1
            else:
                l = mid+1
        return False