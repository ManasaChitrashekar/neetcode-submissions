class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fcount =0 
        tcount = 0 
        for bill in bills:
            if bill ==5:
                fcount +=1
            elif bill == 10:
                tcount +=1
                fcount -=1
            elif tcount > 0:
                tcount -=1
                fcount -=1
            else:
                fcount -=3
            if fcount<0:
                return False
                
        return True
        