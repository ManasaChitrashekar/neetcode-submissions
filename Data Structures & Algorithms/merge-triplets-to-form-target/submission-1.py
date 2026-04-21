class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        a,b,c = target[0],target[1],target[2]
        for t in triplets:
            x,y,z = t[0],t[1],t[2]
            if  x > a or y > b or z > c:
                continue 
            if x == a :
                good.add(0)
            if y == b:
                good.add(1)
            if z == c:
                good.add(2)
        return len(good)==3
           