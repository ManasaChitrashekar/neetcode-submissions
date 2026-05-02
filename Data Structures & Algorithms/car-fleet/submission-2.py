class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        smap = {}
        stack = []
        #pair = [(p, s) for p, s in zip(position, speed)]
        for i in range(len(position)):
            smap[position[i]]=speed[i]
        position.sort(reverse = True)
        for p in position:
            time = (target-p)/smap[p]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
        