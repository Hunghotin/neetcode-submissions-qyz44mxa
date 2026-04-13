"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        intervals.sort(key = lambda x:x.start)
        
        tmp = 0
        for i in range(n):
            if tmp > intervals[i].start:
                return False
            tmp = intervals[i].end
        return True