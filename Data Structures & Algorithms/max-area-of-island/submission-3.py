class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        res = 0
        visited = set()
        def dfs(i,j):
            if i<0 or i==ROWS or j<0 or j==COLS or grid[i][j]==0 or (i,j) in visited:
                return 0 
            visited.add((i,j))
            return 1+dfs(i+1,j)+ dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1 and (i,j) not in visited:
                    res = max(res,dfs(i,j))
        return res 