class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l ,h = 2,x//2
        while l<=h:
            mid = l +((h-l))//2
            res = mid * mid 
            if res == x :
                return mid 
            elif res < x:
                l = mid+1
            else:
                h = mid-1 
        return h

      