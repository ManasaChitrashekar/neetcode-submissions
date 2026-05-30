class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap,-stone)
        while len(maxheap)>1:
            y = abs(heapq.heappop(maxheap))
            x = abs(heapq.heappop(maxheap))
            if x < y:
                heapq.heappush(maxheap,-(y-x))
        return abs(maxheap[0]) if maxheap else 0