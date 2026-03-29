class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = strs[0]
        for i in range(1,len(strs)):
            if len(strs[i]) <= len(small):
                small = strs[i]
        
        lp = ""
        start=""
        for s in small:
            contains = True
            start+=s
            for word in strs:
                if not word.startswith(start):
                    contains=False
                    break
            if contains:
                lp= start
            else:
               break
        return lp
