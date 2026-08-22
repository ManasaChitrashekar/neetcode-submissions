class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        cmap = Counter(nums)
        minheap = []
        for key,count in cmap.items():
            heapq.heappush(minheap,[count,key])
            if len(minheap)>k:
                heapq.heappop(minheap)
        while minheap:
            res.append(heapq.heappop(minheap)[1])
        return res
