# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Merge by keeping track of the current ptr in all lists
        # and putting the nodes in lists into a minPQ
        # Easier if use a sentinel node at start
        ret = ptr = ListNode(-1)
        heap = []
        # initialize heap with the first node val in all lists
        # We push to heap a tuple that contains the idx of the lists
        # this make sure when val is the same it does not need to compare
        # the ListNode object which is not comparable
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, idx, l))
        while heap:
            val, idx, node = heapq.heappop(heap)
            # Only create next node when there is stuff poping from heap
            ptr.next = ListNode(val)
            ptr = ptr.next
            if node.next:
                next_node = node.next
                heapq.heappush(heap, (next_node.val, idx, next_node))
        return ret.next
