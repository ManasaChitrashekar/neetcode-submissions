class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = defaultdict(int)
        for num in nums:
            freqmap[num]= 1+freqmap.get(num,0)
        heap = []
        for key in freqmap.keys():
            heapq.heappush(heap,(freqmap[key],key))
            if len(heap)>k :
                heapq.heappop(heap)
        res =[]
        for i in range(k):
            value,key = heapq.heappop(heap)
            res.append(key)
        return res