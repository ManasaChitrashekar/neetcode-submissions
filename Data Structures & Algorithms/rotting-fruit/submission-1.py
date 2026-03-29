class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0 
        time = 0 
        ROWS,COLS = len(grid),len(grid[0])
        q= deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
                
            
        direction = [[1,0],[-1,0],[0,1],[0,-1]]    
        while q and fresh>0 :
            for j in range(len(q)):
                r,c= q.popleft()
                for nr,nc in direction:
                    nr= nr+r
                    nc=nc+c
                    if nr in range(ROWS) and nc in range(COLS ) and  grid[nr][nc]==1: 
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
        