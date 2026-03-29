class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = Counter(t)
        need = len(tmap)
        have = 0
        res=[-1,-1]
        reslen = float("inf")
        i = 0 
        smap =  defaultdict(int)
        for j in range(len(s)):
            #add to map 
            smap[s[j]]+=1

            #comapre and increament count
            if s[j] in tmap and smap[s[j]]==tmap[s[j]]:
                have+=1
            #check window size reached and try to shrink 
            while have==need:
                if j-i+1 < reslen:
                    res = [i,j]
                    reslen = j-i+1
                smap[s[i]]-=1
                if s[i] in tmap and smap[s[i]]<tmap[s[i]]:
                    have-=1
                i+=1

            

        return s[res[0]:res[1]+1] if res[0]!=-1 else ""
