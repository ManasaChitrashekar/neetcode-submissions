class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        counter = 0
        i=0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                str1 = words[i]
                str2 = words[j]
                
                # Check if str1 is both a prefix and a suffix of str2
                if str2.startswith(str1) and str2.endswith(str1):
                    counter += 1
        return counter