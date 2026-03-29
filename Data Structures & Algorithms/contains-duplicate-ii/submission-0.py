class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = {}
        i=0
        for num in nums:
            if (num  in unique and unique[num]!=i and i-unique[num]<=k):
                return True
            unique[num]= i 
            i+=1
        return False