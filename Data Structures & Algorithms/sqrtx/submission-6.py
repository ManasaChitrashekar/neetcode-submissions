class Solution:
    def mySqrt(self, x: int) -> int:
            if x < 2:
                return x
            #sqrt of number cant be greated than x//2
            l,h = 2,x//2
            while l <=h:
                mid = l+(h-l)//2
                num = mid * mid 
                if num == x:
                    return mid 
                elif num < x:
                    l = mid +1
                else:
                    h = mid - 1
            return h
      