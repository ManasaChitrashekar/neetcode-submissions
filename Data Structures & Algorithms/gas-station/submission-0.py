class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
            if sum(gas)<sum(cost):
                return -1 
            total = 0
            res =0 
            for i in range(len(gas)):
                total += gas[i]-cost[i] 
                if total<0:
                    #I cant start here so reset total and try next position
                    total = 0 
                    res =i+1
            return res