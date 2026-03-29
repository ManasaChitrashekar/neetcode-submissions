class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        subStringSet = set()
        for r in range(len(s)):
            while(s[r] in subStringSet):
                subStringSet.remove(s[l])
                l = l +1
            subStringSet.add(s[r])
            longest = max(longest,r-l+1)
        return longest

        