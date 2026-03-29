class Solution:
    def isValid(self, s: str) -> bool:
        bdict = {"(":")","{":"}","[":"]"}
        stack = []
        for c in s:
            if c  in  "({[":
                stack.append(c)
            else:
                if stack and bdict[stack[-1]]==c:
                    stack.pop()
                else:
                    return False
        return False if stack else True
       
        