class Solution:
    def checkValidString(self, s: str) -> bool:
        minb,maxb = 0,0
        for c in s:
            if c == "(":
                minb,maxb = minb+1,maxb+1
            elif c == ")":
                minb,maxb = minb-1,maxb-1
            else:
                #what possible values i coud choose [-1,0,1] syaing it can be treates as ) "" ( since this is range if min goes -ve lets ignore and reset saying we choose nothing 
                minb,maxb = minb-1,maxb+1
            if maxb < 0:
                return False
            if minb < 0:
                minb = 0
                
        return minb == 0 