class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        uni = set()
        i = 0 
        for j in range(len(s)):
            while  s[j] in uni:
                uni.remove(s[i])
                i +=1
            uni.add(s[j])
            res = max (res,j-i+1)
        return res 