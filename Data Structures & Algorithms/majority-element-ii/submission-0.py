class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        fmap = Counter(nums)
        size = len(nums)//3
        res = []
        for k,v in fmap.items():
            if v > size:
                res.append(k)
        return res