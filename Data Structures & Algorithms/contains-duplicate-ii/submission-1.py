class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = {}
        for i in range(len(nums)):
            if nums[i] in unique and unique[nums[i]]!= i and abs(unique[nums[i]]-i)<=k:
                return True
    
            unique[nums[i]]=i
        return False