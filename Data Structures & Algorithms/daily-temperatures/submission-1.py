class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                res.insert(0,stack[-1][1]-i)
            else:
                res.insert(0,0)
            stack.append([temperatures[i],i])
        return res    