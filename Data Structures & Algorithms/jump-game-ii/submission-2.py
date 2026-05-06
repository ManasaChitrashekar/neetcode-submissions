class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curend = 0
        maxfar = 0 
        #jump when i reach fence or exhaust the no if jumps i made happend when i == curend
        for i in range(len(nums)-1):
            maxfar = max(maxfar, i + nums[i])   # "how far could I reach from here?"
            if i == curend:                          # "did I hit the fence?"
                jumps += 1; 
                curend = maxfar        # "jump! move fence forward"
        return jumps