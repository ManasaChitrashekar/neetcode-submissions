class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        maxlen = 0 
        uni = set()
        for j in range(len(s)):
                while s[j] in uni:
                    uni.remove(s[i])
                    i+=1
                    
                uni.add(s[j])
                maxlen = max(maxlen,j-i+1)
        return maxlen