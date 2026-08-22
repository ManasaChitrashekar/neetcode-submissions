class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqset = set() 
        for num in nums:
            if num in uniqset :
                return True
            uniqset.add(num)
        return False