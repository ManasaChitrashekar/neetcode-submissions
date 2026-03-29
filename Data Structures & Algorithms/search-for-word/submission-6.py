class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS = len(board),len(board[0])
        def dfs(row,col,i):
            if i == len(word):
                return True
            if (row<0 or col<0 or row>=ROWS or col>=COLS or
             board[row][col]!= word[i] or board[row][col] == '#'):
                return False
            
            board[row][col] = '#'
            res = (dfs(row+1,col,i+1) or 
                  dfs(row-1,col,i+1)  or 
                  dfs(row,col+1,i+1) or 
                  dfs(row,col-1,i+1) )
            #undo the coard
            board[row][col]=word[i]
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        
        return False