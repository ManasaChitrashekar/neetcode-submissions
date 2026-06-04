class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        posmap = defaultdict(int)
        res = []
        for i,c in enumerate(s):
            posmap[c]= i 
        end = 0 
        size =0 
        for i,c in enumerate(s):
            size +=1
            end = max(end,posmap[c])
            if i ==end :
                res.append(size)
                size = 0
        return res
        