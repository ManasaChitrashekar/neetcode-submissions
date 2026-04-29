class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS ,COLS = len(grid),len(grid[0])
        minheap = []
        heapq.heappush(minheap,(grid[0][0],0,0)) 
        #height , r,c
        visited = set()
        visited.add((0,0))
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        while minheap:
            time,r,c = heapq.heappop(minheap)
            visited.add((r,c))
            if (r,c)==(ROWS-1,COLS-1):
                return time
            for m,n  in  dir:
                rm,cn = m+r,n+c
                if 0 <= rm < ROWS and 0 <= cn < COLS and (rm,cn) not in visited:
                    visited.add((rm,cn))
                    heapq.heappush(minheap,(max(time,grid[rm][cn]),rm,cn))
                    
        

