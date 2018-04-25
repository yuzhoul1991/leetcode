# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        intervals.sort(key=lambda x: x.start)
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            prev = ret[-1]
            if interval.start <= prev.end:
                # Notice the use of max here in case the new interval
                # is completely inside the prev interval
                # cannot just assign with interval.end
                prev.end = max(prev.end, interval.end)
            else:
                ret.append(interval)
        return ret
        
