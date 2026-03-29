class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alist = defaultdict(list)

        for s in strs:
             key = "".join(sorted(s))
             alist[key].append(s)
        return list(alist.values())