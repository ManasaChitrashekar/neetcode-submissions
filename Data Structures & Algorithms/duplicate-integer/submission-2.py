class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uni = set(nums)
        return len(uni)!=len(nums)