class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = Counter(nums)
        maxheap = []
        for key,freq in countmap.items():
            heapq.heappush(maxheap,(-freq,key))
        res=[]
        for i in range(k):
            res.append(heapq.heappop(maxheap)[1])
        return res