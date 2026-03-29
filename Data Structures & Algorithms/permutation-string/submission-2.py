class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            start,end=0,0
            s1map = {}
            s2map = {}
            for i in range(len(s1)):
                s1map[s1[i]]= 1+s1map.get(s1[i],0)
            for end in range(len(s2)):
                s2map[s2[end]]= 1+s2map.get(s2[end],0)
                if(end-start+1==len(s1)):
                    if(s1map == s2map):
                        return True
                if(end-start+1>len(s1)):
                    if(s2map.get(s2[start])):
                        s2map[s2[start]]= s2map.get(s2[start])-1
                    if(s2map.get(s2[start])==0):
                        s2map.pop(s2[start])
                    start+=1
                    if(s1map == s2map):
                        return True
            return False