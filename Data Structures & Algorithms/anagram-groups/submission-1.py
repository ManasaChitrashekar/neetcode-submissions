from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        freq_dict = defaultdict(list)
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch)-ord('a')]+=1
            key = tuple(count)    
            freq_dict[key].append(word)

        return list(freq_dict.values())        
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        