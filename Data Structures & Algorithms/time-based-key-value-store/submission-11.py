class TimeMap:

    def __init__(self):
        self.count = 1
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap[key]
        n = len(values)
        if len(values)==0:
            return ""
        l,h = 0,n-1
        res = ""
        while l <=h:
            m = (l+h) //2
            if values[m][1] <= timestamp:
                res  =values[m][0]
                l = m+1
            else:
                h = m-1
        return res
