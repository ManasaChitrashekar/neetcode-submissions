class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        l = 0 
        h = (rows*cols) - 1
        while l<=h:
            mid = l + (h-l)//2
            r,c = mid//cols,mid%cols
            if matrix[r][c]==target:
                return True
            if matrix[r][c]<target:
                l = mid+1
            else:
                h = mid-1
        return False