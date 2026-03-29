class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc = enc+str(len(s))+'#'+s
        return enc

    def decode(self, s: str) -> List[str]:
        res = []
        i =0
        while(i<len(s)):
            j = s.find("#",i)
            if j == -1:
                break
            count = int(s[i:j])
            decode = s[j+1:j+1+count]
            res.append(decode)
            i = j+1+count
        return res

