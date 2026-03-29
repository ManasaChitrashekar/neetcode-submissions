class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0,len(people)-1
        res = 0 
        # 1,2,2,3,3 r= 3
        # 1,2,2,3,3 r=2
        # 1,2,2,3,3 
        while l <= r:
            if r!=l and people[l]+people[r] <=limit:
                res +=1
                l +=1
                r -=1
            elif people[r]<=limit:
                res +=1
                r -=1
            elif people[l]<=limit:
                res +=1
                l +=1
        return res 