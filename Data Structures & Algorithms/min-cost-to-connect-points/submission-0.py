class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #build adjacency list 
        #do bfs using min heap , res is obtained when visted = len(points)
        n = len(points)
        adjmap = defaultdict(list)
        for i in range(n):
            x1,y1 = points[i][0],points[i][1]
            for j in range(i+1,n):
                x2,y2 = points[j][0],points[j][1]
                elen = abs(x2-x1)+abs(y2-y1)
                adjmap[i].append([j,elen])
                adjmap[j].append([i,elen])
        visited = set()
        minheap = []
        heapq.heappush(minheap,[0,0])
        res = 0 
        while len(visited) < n:
            cost,node = heapq.heappop(minheap)
            if node in visited:
                continue
            res +=cost
            visited.add(node)
            for nei,neiCost in adjmap[node]:
                if nei not in visited :
                    heapq.heappush(minheap,[neiCost,nei])
        return res