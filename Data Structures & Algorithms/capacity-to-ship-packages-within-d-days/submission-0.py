class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low ,high = max(weights),sum(weights)
        while(low<high):
            rate = (low+high)//2
            count = 1
            tw = 0 
            for w in weights:
                tw +=w
                if tw > rate:
                    count +=1
                    tw = w
            if(count<=days):
                high= rate 
            else:
                low = rate +1    
        return high         