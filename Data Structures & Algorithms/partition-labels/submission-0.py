class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        pmap = defaultdict(int)
        for i in range(len(s)):
            pmap[s[i]] = i
        size,end  = 0,0
        for i in range(len(s)):
            size +=1
            end = max(end,pmap[s[i]])
            if i == end:
                res.append(size)
                size = 0 
        return res

            