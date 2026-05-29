class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        cmap = Counter(nums)
        maxheap = []
        for key,val in cmap.items():
            heapq.heappush(maxheap,[-val,key])
        while k > 0:
            res.append(heapq.heappop(maxheap)[1])
            k -=1
        return res
