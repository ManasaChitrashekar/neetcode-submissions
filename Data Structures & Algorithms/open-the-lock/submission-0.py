class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque()
        q.append("0000")
        visited = set(deadends)
        turns = 0 
        def children(lock):
            res = []
            for i in range(len(lock)):
                digitstr = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digitstr + lock[i+1:])

                digitstr = str((int(lock[i]) - 1+10) % 10)
                res.append(lock[:i] + digitstr + lock[i+1:])
            return res 
        while q:
            for i in range(len(q)):
                keyc = q.popleft()
                if keyc == target:
                    return turns
                for child in children(keyc):
                    if child not in visited:
                        q.append(child)
                        visited.add(child)
            turns +=1

        return -1 