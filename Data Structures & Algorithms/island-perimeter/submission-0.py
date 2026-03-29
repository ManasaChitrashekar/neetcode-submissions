class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
            rows,cols = len(grid),len(grid[0])
            visited = set()
            def dfs(i,j):
                if (i,j) in visited:
                    return 0 
                if i < 0 or i==rows or j<0 or j==cols or grid[i][j]==0 :
                    return 1
                visited.add((i,j))
                return dfs(i+1,j)+dfs(i-1,j)+dfs(i,j-1)+dfs(i,j+1)
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j]==1:
                        return dfs(i,j)
            return 0
            