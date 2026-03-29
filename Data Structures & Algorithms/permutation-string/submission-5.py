from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = Counter(s1)
        i=0
        s2map = defaultdict(int)
        for j in range(len(s2)):
            s2map[s2[j]]+=1
            while(j-i+1>len(s1)):
                s2map[s2[i]]-=1
                if(s2map[s2[i]]==0) :
                    del s2map[s2[i]]
                i+=1
            if(s1map==s2map):
                return True
        return False
        
       
    
        