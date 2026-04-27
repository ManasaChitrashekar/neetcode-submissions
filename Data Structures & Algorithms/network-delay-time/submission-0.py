class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjmap =defaultdict(list)
        for u,v,t in times:
            adjmap[u].append([v,t])
        t = 0 
        minheap = []
        heapq.heappush(minheap,(0,k))
        visited = set()
        while minheap:
            w1,node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            t = w1
            for n1,t1 in adjmap[node]:
                if n1 not in visited:
                     heapq.heappush(minheap,(w1+t1,n1))
        return t if len(visited)==n else -1