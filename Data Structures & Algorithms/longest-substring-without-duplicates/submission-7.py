class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen =0
        start,end=0,0
        subset = set()
        for end in range(len(s)):
            while(s[end] in subset):
                subset.remove(s[start])
                start+=1
            maxlen = max(maxlen,end-start+1)    
            subset.add(s[end])    
        return maxlen    