class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                ch = ""
                while stack and stack[-1]!="[":

                    ch = stack.pop()+ ch
                stack.pop()
                num = ""
                while  stack and (stack[-1]).isdigit():
                    num = (stack.pop()) +num

                stack.append(ch * int(num))
        return "".join(stack)