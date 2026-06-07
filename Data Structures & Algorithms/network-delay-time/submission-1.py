class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build map 
        amap = defaultdict(list)
        for u,v,w in times:
            amap[u].append([v,w])
        
        minheap = []
        heapq.heappush(minheap,(0,k))
        visited = set()
        time =0 
        while minheap:
            tw,node = heapq.heappop(minheap)
            if node in visited:
                continue
            time = tw
            visited.add(node)
            for nei,w in amap[node]:
                heapq.heappush(minheap,(tw+w,nei))
        return time if len(visited)==n else -1