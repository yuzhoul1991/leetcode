class MyCalendarTwo(object):
    """
    Maintain a list of intervals and also maintain a list of overlaps
    if a new interval overlaps with one of the overlaps, then it is triple book
    after a successful insersion, need to check with other intervals to update overlaps
    """
    def __init__(self):
        self.intervals = []
        self.double_book = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.double_book:
            if start < j and end > i:
                return False
        # okay to insert at this point, update double_book
        for i, j in self.intervals:
            if start < j and end > i:
                self.double_book.append((max(i, start), min(j, end)))
        self.intervals.append((start, end))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
