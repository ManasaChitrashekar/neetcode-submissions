class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fcount =0 
        tcount = 0 
        for bill in bills:
            if bill ==5 :
                fcount +=1
            elif bill ==10:
                if fcount==0:
                    return False
                else :
                    fcount -=1
                    tcount  +=1
            elif bill==20:
                if tcount != 0 and fcount!=0:
                    tcount -=1
                    fcount -=1
                elif fcount >=3:
                    fcount -=3
                else:
                    return False
        return True
        