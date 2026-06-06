class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            nums1,nums2 = nums2,nums1
        m,n = len(nums1),len(nums2)
        cutat = (m+n)//2
        l,h = 0 ,m-1
        while True:
            mid = (l+h)//2
            rhalf = cutat-mid -2
            Aleft = nums1[mid] if mid >=0 else float("-inf")
            Aright = nums1[mid+1] if mid+1 < m else float("inf")
            Bleft = nums2[rhalf] if rhalf >=0 else float("-inf")
            Bright = nums2[rhalf+1] if rhalf+1 < n else float("inf")
            if Aleft <= Bright and Bleft <= Aright:
                if (m+n)%2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft > Bright:
                h = mid -1
            else :
                l = mid +1 
       