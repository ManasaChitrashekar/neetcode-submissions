class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        ns,ne = newInterval[0],newInterval[1]
        for start,end in intervals:
            if ne < start :
                res.append([ns,ne])
                ns,ne = start,end 
            elif ns >end:
                res.append([start,end])
            else:
                ns = min(ns,start)
                ne = max(ne,end)
        res.append([ns,ne])
        return res 
