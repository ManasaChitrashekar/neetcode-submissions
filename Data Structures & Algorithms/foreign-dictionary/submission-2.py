class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #bfh with topologicla sort 
        #build indegree and adjaceny list 
        indegree = {}
        premap = defaultdict(set)
        for word in words:
            for c in word:
                indegree[c] = 0
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            # abc ,ab
            if len(w1)> len(w2) and w1.startswith(w2):
                return ""
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    if w2[j] not in premap[w1[j]]:
                        premap[w1[j]].add(w2[j])
                        indegree[w2[j]] +=1
                    break;
        res = []
        q = deque()
        for c,v in indegree.items():
            if v==0:
                q.append(c)
        while q:
                c = q.popleft()
                res.append(c)
                for nei in premap[c]:
                    indegree[nei] -=1
                    if indegree[nei]==0:
                        q.append(nei)
                    
        return "".join(res) if len(res)==len(indegree) else ""

