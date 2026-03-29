class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequencymap = Counter(nums)
        n = len(nums)
        for key,value in frequencymap.items():
            if value > (n//2):
                return key
        return O