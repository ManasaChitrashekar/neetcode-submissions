class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")]*n
        prices[src]=0
        for i in range(k+1):
            temp = prices.copy()
            for s,d , c in flights:
                if prices[s]+c < temp[d]:
                    temp[d]=prices[s]+c
            prices = temp 
        return prices[dst] if prices[dst]!=float("inf") else -1

#DJIKSTRAS

#         import heapq
# from collections import defaultdict

# def findCheapestPrice(n, flights, src, dst, k):
#     adj = defaultdict(list)
#     for u, v, w in flights:
#         adj[u].append((v, w))
    
#     # (cost, node, stops)
#     heap = [(0, src, k + 1)]
    
#     while heap:
#         cost, node, stops = heapq.heappop(heap)
        
#         if node == dst:
#             return cost
        
#         if stops > 0:
#             for nei, price in adj[node]:
#                 heapq.heappush(heap, (cost + price, nei, stops - 1))
    
#     return -1