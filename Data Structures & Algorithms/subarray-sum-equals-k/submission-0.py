class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res ,sum = 0,0
        prefixmap = defaultdict(int)
        prefixmap[0]=1
        for num in nums:
            sum += num 
            if prefixmap[sum-k]:
                res += prefixmap[sum-k]
            prefixmap[sum] += 1
        return res
        