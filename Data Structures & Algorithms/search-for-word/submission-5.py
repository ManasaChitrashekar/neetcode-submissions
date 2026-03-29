class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,index) :
            if index == len(word):
                return True
            #if goes out of bound 
            if (r<0 or c<0 or r>=row or c>=col or board[r][c] != word[index]):
                return False

            temp = board[r][c]
            board[r][c] = "#"
            
            ans = dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c+1,index+1) or dfs(r,c-1,index+1)

            board[r][c] = temp
            return ans  

        #find first occurance of the word
        row,col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if(board[i][j]==word[0]):
                      if dfs(i, j, 0):  # If we find the word starting from this cell
                        return True
        return False
    
        