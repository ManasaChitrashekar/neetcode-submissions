class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        i=0
        res = 0 
        for j in range(len(s)):
            while s[j] in unique :
                unique.remove(s[i])
                i+=1
            res = max(res,j-i+1)
            unique.add(s[j])
        return res