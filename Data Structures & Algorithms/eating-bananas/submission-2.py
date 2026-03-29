class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low ,high = 1,max(piles)
        res = high 
        while(low<=high):
            rate = (low+high)//2
            k=0
            for i in range(len(piles)):
                k = k + math.ceil(float(piles[i])/rate)
            if(k<=h):
                res = rate
                high= rate -1
            else:
                low = rate +1    
        return res         