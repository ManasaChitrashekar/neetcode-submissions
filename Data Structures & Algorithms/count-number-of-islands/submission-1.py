class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])
        res = 0 

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c]="0"
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                row,col = q.popleft()
                for i,j in directions:
                    i , j = i+row,j+col
                    if  i < rows and j <cols  and i >=0 and j>=0 and grid[i][j]!= "0"  :
                        q.append((i,j))
                        grid[i][j]="0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" :
                    res+=1
                    bfs(r,c)
        return res