class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        small = strs[0]
        for i in range(1,len(strs),1):
            pre = strs[i]
            j = 0 
            while j < len(small) and small[j]==pre[j]:
                j +=1
            small = small[:j]
        return small
