class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = defaultdict(list)
        path,visited = set(),set()
        order = []
        for u, v in prerequisites:
            premap[u].append(v)
        def dfs(i):
            if i in path:
                return False
            if i in visited:
                return True 
            path.add(i)
            for j in premap[i]:
                if not dfs(j):
                    return False
            visited.add(i)
            order.append(i)
            path.remove(i)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return order 