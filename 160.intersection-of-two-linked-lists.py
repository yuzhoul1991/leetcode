# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Use two pointers and initialize them to headA/headB
        # when either is exhausted its list, redirect it to the other list
        # they either end up with same val node
        # or end up at the end of list at the same time on 2nd iteration
        if not headA or not headB: return None
        ptr1, ptr2 = headA, headB
        while ptr1 != ptr2:
            ptr1 = ptr1.next if ptr1 else headB
            ptr2 = ptr2.next if ptr2 else headA
        return ptr1

        
