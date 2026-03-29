class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, h = 0,len(arr)-k
        while l<h:
            m = (l+h)//2
            if x-arr[m] > arr[m+k]-x:
                l = m+1
            else:
                h = m 
        return arr[l:l+k]
