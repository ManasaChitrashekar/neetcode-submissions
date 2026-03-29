class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       lookup = {}
       res = 0
       maxF = 0
       start,end = 0,0
       for end in range(len(s)):
           lookup[s[end]] = 1+  lookup.get(s[end],0)
           maxF = max(lookup.get(s[end]),maxF)
           while(end-start+1-maxF>k):
                if(lookup[s[start]]>0):
                    lookup[s[start]]-= 1
                else:
                    lookup.remove[s[end]]  
                start+=1
           res = max(res,end-start+1)
       return res 