class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op=="+":
                first = stack[-1]
                second = stack[-2]
                print(first+second)
                stack.append(first+second)
            elif op=="D":
                first = stack[-1]
                stack.append(first*2)
            elif op=="C":
                first = stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)