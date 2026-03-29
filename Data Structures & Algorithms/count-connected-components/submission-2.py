class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1]*n 

        def find(n1):
            if par[n1] != n1:
                par[n1] = find(par[n1])  # path compression
            return par[n1]

        def union(u,v):
            n1,n2= find(u),find(v)
            if n1==n2:
                return 
            if rank[n1]>rank[n2]:
                par[n2]=n1
                rank[n1]+=rank[n1]
            else :
                par[n1]=n2
                rank[n2]+=rank[n2]
            nonlocal res
            res -=1    
            return 
        res = n
        for u,v in edges:
           union(u,v)
        return res