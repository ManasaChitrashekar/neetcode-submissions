class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        iplist = []
        def dfs(i,dcount,cur):
            if dcount ==4 and i ==len(s):
                iplist.append(cur[:-1])
                return 
            if dcount > 4:
                return 
            for j in range(i,min(i+3,len(s))):
                part = s[i:j+1]
                if  len(part)> 1 and part[0]=="0" : 
                    continue
                if  int(part) >= 256:
                    continue
                dfs(j+1,dcount+1,cur+part+".")
        dfs(0,0,"")
        return iplist
