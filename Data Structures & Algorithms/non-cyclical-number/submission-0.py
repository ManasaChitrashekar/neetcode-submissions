class Solution:
    def isHappy(self, n: int) -> bool:
        single = set()
        
        def getsingle(n):
            res = 0
            while n > 9  :
                rem = n % 10
                res += rem * rem 
                n = n//10 
            return res +(n*n)
        while(1) :
            res = getsingle(n)
            if res == 1:
                return True 
            if res and res <= 9:
                if res in single :
                    return False
                single.add(res)
            n = res 

        

        