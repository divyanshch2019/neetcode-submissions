"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def overlap(self,a,b):
        return not (b.start>=a.end or a.start>=b.end)
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        for i in range(1,len(intervals)):
            if self.overlap(intervals[i-1],intervals[i]):
                return False
        return True

