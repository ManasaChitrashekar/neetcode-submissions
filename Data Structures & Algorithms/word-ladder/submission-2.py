class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        #o(m square * n) n is number of words m in len of each word 
        #["hit"]
        #["hot", "lit"]
        #["dot", "lot", ...]
        if endWord not in wordList :
            return 0 
        
        patternmap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern= word[:j]+"*"+word[j+1:]
                patternmap[pattern].append(word)
        q = deque()
        visited = set()
        visited.add(beginWord)
        q.append(beginWord)
        res =1
        while q:
            qlen = len(q)
            for _ in range(qlen):
                popped = q.popleft()
                if popped == endWord:
                    return res
                for j in range(len(popped)):
                    pattern= popped[:j]+"*"+popped[j+1:]
                    wordlist = patternmap[pattern]
                    for nei in wordlist:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res +=1
        return 0
        
