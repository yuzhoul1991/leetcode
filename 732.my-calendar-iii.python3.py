class MyCalendarThree:
    """
    Use a hsh to store start and end count
    when there is an event start, end
    hsh[start] += 1; hsh[end] -= 1 to record how many events happened and ended on timestamp
    When new even gets inserted, replay all previous events in chronilogical order, keep count of how many events are going on at a time
    """

    def __init__(self):
        self.events = collections.defaultdict(int)    

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # First insert the event
        self.events[start] += 1
        self.events[end] -= 1
        concurrent_events = 0
        ret = 0
        for time in sorted(self.events.keys()):
            concurrent_events += self.events[time]
            ret = max(ret, concurrent_events)
        return ret

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
