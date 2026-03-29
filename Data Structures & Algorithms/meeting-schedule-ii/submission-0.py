"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval:interval.start)
        res = []
        for interval in intervals:
            if res and res[0]<= interval.start :
                heapq.heappop(res)
            heapq.heappush(res,interval.end)
        return len(res)