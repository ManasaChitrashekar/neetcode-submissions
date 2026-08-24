class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #for any position prefix sum is prefix sum to left and above it 
        ROWS,COLS = len(matrix),len(matrix[0])
        self.prefixmatrix = [[0]*(COLS+1) for r in range(ROWS+1)]
        for r in range(ROWS):
            prefixsum = 0 
            for c in range(COLS):
                prefixsum += matrix[r][c]
                above = self.prefixmatrix[r][c+1]
                self.prefixmatrix[r+1][c+1]=prefixsum+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefixmatrix[row2 + 1][col2 + 1]
        above = self.prefixmatrix[row1][col2+1]
        left = self.prefixmatrix[row2+1][col1]
        topleft = self.prefixmatrix[row1][col1]
        return bottomRight-above-left+topleft
    



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)