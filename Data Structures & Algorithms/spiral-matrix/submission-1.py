class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,left = 0,0
        bottom,right = len(matrix),len(matrix[0])
        res = []
        while left<right and top<bottom:
            #tarverse first left to right 
            for i in range(left,right):
                res.append(matrix[top][i])
            top +=1
            #traverse top to bottom
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right -=1
            #traverse right to left 
            if top < bottom:
                for i in range(right-1,left-1,-1):
                    res.append(matrix[bottom-1][i])
                bottom -=1
            if left < right:
                for i in range(bottom-1,top-1,-1):
                    res.append(matrix[i][left])
                left +=1
        return res