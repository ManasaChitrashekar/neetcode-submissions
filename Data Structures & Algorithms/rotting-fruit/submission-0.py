class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        fresh = 0 
        res =0
        q= deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh+=1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    q.append((i,j))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while fresh>0 and q:
            for j in range(len(q)):
                # fruit +1 is fruit mark as 2 and append to q dec fresh  
                r,c = q.popleft()
                for nr,nc in directions:
                    row,col = nr+r,nc+c
                    if row in range(ROWS) and col in range(COLS) and grid[row][col]==1:
                        fresh-=1
                        grid[row][col]=2
                        q.append((row,col))
            res+=1
        
        return res if fresh == 0 else -1