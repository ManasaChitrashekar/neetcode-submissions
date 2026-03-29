class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        parent = [i for i in range(n)]
        rank = [0]*n

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            rx = find(x)
            ry = find(y)
            if rx == ry :
                return True
            if rank[rx]>rank[ry]:
                parent[ry]=rx
            elif rank[rx]<rank[ry]:
                parent[rx]=ry
            else:
                parent[ry]=rx
                rank[rx] +=1
            return False
        for u,v in edges:
            if  union(u,v):
                return [u,v]
        #check all the nodes have same connected root , tree cant have disconnected node 
       