class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # CHECK: a tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        par = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])   # path compression
            return par[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return True  # cycle detected
            if rank[pa] > rank[pb]:
                par[pb] = pa
            elif rank[pb] > rank[pa]:
                par[pa] = pb
            else:
                par[pb] = pa
                rank[pa] += 1
            return False

        for u, v in edges:
            if  union(u, v):
                return False

        return True 
