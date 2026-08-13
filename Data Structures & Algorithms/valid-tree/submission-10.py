class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)> n-1:
            return False
        rank = [0]*n
        parent = [i for i in range(n)]


        def find(u):
            if parent[u]!=u:
                parent[u]=find(parent[u])
            return parent[u]


        def union(u,v):
            x = find(u)
            y = find(v)
            if x==y:
                return False
            if rank[x] >= rank[y]:
                parent[y]=x
                rank[x]+=1
            else:
                parent[x]=y
                rank[y]+=1
            return True


        #check if there is cycle when creating edges
        for u,v in edges:
            if not union(u,v):
                return False
        root = find(0)
        for i in range(n) :
            if find(i)!=root:
                return False
        return True 