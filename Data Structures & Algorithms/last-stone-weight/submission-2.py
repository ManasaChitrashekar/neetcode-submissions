import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)
            if(x>y):
                heapq.heappush(maxHeap,y-x)
        maxHeap.append(0)      
        return abs(maxHeap[0])       