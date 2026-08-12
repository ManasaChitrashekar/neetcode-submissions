class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        adjmap = defaultdict(list)
        for course,preq in prerequisites:
            adjmap[course].append(preq)
        def dfs(crs):
            if crs in path:
                return False
            if adjmap[crs] == []:
                return True
            path.add(crs)
            for pre in adjmap[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            adjmap[crs]= []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True