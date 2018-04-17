class MyCalendar(object):
    # A BST class that can be used to store the intervals ordered by start of 
    # the interval
    class TreeNode(object):
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.left = self.right = None

        def insert(self, node):
            start, end = node.start, node.end
            # Since there is no overlap allowed only two cases can allow insert
            # 1. start is larger than or equal to my end
            # 2. end is less than or equal to my start
            # goes right
            if start >= self.end:
                if not self.right:
                    self.right = node
                    return True
                else: 
                    return self.right.insert(node)
            # goes left
            elif end <= self.start:
                if not self.left:
                    self.left = node
                    return True
                else:
                    return self.left.insert(node)
            else:
                return False
                

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = self.TreeNode(start, end)
            return True
        else:
            return self.root.insert(self.TreeNode(start, end))
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
