class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first+second)
            elif s == "-":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first-second)
            elif s == "*":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first*second)
            elif s == "/":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(int(first/second))
            else:
                stack.append(int(s))
        return stack[-1]