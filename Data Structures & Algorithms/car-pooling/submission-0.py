class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cmap = defaultdict(int)
        for trip  in trips:
            passangers,start,end= trip[0],trip[1],trip[2]
            cmap[start] += passangers
            cmap[end] -= passangers
        
        cur = 0 
        for pos in sorted(cmap):
            cur +=cmap[pos]
            if cur > capacity:
                return False
        return True
     