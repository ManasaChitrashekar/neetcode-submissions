import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for point in points:
            distance = -((point[0]*point[0]) + (point[1]*point[1]))
            heapq.heappush(maxheap,[distance,point])
            if(len(maxheap)>k):
                heapq.heappop(maxheap)
               
        res = []
        for value in maxheap:
            res.append(value[1])  
        return res         