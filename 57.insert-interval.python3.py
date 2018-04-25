# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # Use binary search to locate the index that newInterval should be inserted
        # then merge the intervals together
        # insert
        starts = list(map(lambda x: x.start, intervals))
        idx = bisect.bisect_left(starts, newInterval.start)
        intervals.insert(idx, newInterval)
        # merge
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = ret[-1]
            interval = intervals[i]
            if interval.start <= prev.end:
                prev.end = max(prev.end, interval.end)
            else:
                ret.append(interval)
        return ret

        
