class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-i for i in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            y = -1*heapq.heappop(maxheap)
            x = -1*heapq.heappop(maxheap)
            if y-x>0:
                heapq.heappush(maxheap,-1*(y-x))
        return maxheap[0]*-1 if maxheap else 0