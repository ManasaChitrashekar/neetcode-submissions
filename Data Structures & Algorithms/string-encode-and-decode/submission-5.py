class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            dec = str(len(word))+"#"+word
            s += dec
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        i,j =0,0
        res = []
        while j<len(s):
            if s[j]=="#":
                print(i,j)
                count = int(s[i:j])
                word = s[(j+1):(j+count+1)]
                print(word)
                res.append(word)
                j= j+count+1
                i = j
            else:
                j +=1
        return res

