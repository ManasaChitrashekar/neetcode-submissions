class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curend = 0
        maxfar = 0 
        #jump when i reach fence or exhaust the no if jumps i made happend when i == curend
        for i in range(len(nums)-1):
            maxfar = max(maxfar,i+nums[i])
            #jump only if i cant reuse my cur end 
            if i == curend:
                curend = maxfar
                jumps +=1
        return jumps