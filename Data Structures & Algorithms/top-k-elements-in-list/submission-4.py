class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countermap = Counter(nums)
        maxheap =[]
        res = []
        for key,val in countermap.items():
            heapq.heappush(maxheap,[-val,key])
        for i in range(k):
           val,key = heapq.heappop(maxheap)
           res.append(key)
        return res 