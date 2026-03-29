class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x,y in points:
            dist = -((x*x)+(y*y))
            heapq.heappush(minheap,[dist,x,y])
            
        while len(minheap)>k:
            heapq.heappop(minheap)
        res = []
        for dis,x,y in minheap:
            res.append([x,y])
        return res