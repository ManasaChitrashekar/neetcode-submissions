class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxf = 0 
        i = 0
        count = defaultdict(int)

        def maxv(count):
            maxc = 0
            for v in count.values():
                maxc = max(maxc,v)
            return maxc 

        for j in range(len(s)):
            count[s[j]]+=1
            maxf = max(maxf,maxv(count))
            while j-i+1-maxf > k :
                count[s[i]]-=1
                i+=1
            res = max( res,j-i+1)
        return res

        