class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)> n-1:
            return False
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
                return False
            if rank[rx]>=rank[ry]:
                parent[ry]=rx
                rank[rx] +=1
            elif rank[rx]<rank[ry]:
                parent[rx]=ry
                rank[ry] +=1
           
               
            return True
        for u,v in edges:
            if not union(u,v):
                return False
        #check all the nodes have same connected root , tree cant have disconnected node 
        root = find(0)
        for i in range(1,n):
            if find(i)!=root:
                return False
        return True