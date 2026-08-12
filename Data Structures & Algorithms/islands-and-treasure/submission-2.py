class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        dist = 0 
        visited = set()

        
        ROWS ,COLS = len(grid),len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))
        
        def add(i,j):
            if i < 0 or i == ROWS or j<0 or j ==COLS or grid[i][j]==-1 or (i,j) in visited:
                return 
            visited.add((i,j))
            q.append([i,j])

        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                grid[i][j]=dist
                add(i+1,j)
                add(i-1,j)
                add(i,j+1)
                add(i,j-1)
            dist +=1
        