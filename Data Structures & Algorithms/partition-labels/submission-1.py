class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastpos = {}
        for i,c in enumerate(s):
            lastpos[c]=i
        print(lastpos)
        start,end = 0,0
        for i,c in enumerate(s):
            end = max(end,lastpos[c])
            if i == end:
                res.append(end-start+1)
                start = i+1
        return res 