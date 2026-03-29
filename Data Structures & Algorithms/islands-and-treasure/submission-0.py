class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid),len(grid[0])
        visited = set()
        q = deque()

        def add(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c]==-1 or (r,c) in visited :
                return
            visited.add((r,c))
            q.append((r,c))
        #start bfs parallely on all cells that are gates and fill 
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    q.append((i,j))
                    visited.add((i,j))
         #first is 0 cos we dont conside gate itself
        dist = 0
        while q:
            for k in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=dist
                add(r+1,c)
                add(r-1,c)
                add(r,c-1)
                add(r,c+1)
            dist+=1