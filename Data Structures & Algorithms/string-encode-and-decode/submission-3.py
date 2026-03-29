class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            dec = str(len(word))+"#"+word
            s += dec
        return s

    def decode(self, s: str) -> List[str]:
        i = 0 
        res  = []
        while i<len(s):
            j = i
            while s[j]!="#":
                j +=1
            count = int(s[i:j])
            res.append(s[j+1:count+j+1])
            i = count+j+1
            
        return res 
        