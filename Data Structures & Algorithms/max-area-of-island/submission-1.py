class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        res = 0 

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c]=0
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            area = 1
            while q:
                row,col = q.popleft()
                for i,j in directions:
                    i , j = i+row,j+col
                    if  i < rows and j <cols  and i >=0 and j>=0 and grid[i][j]!= 0  :
                        q.append((i,j))
                        grid[i][j]=0
                        area+=1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 :
                    res = max(res,bfs(r,c))
        return res