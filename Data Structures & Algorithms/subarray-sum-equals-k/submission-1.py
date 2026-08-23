class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixmap = defaultdict(int)
        prefixmap[0]=1
        prefixsum = 0 
        res = 0 
        for num in nums:
            prefixsum +=num 
            #can i find a subarray which i can chop off to get k
            #we can get the chop off part by taking diff of #prefixsum-k
            diff = prefixsum-k
            res += prefixmap[diff]
            prefixmap[prefixsum] +=1
            
        return res