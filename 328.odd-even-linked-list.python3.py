# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # use two pointers and use another pointer to remember what the even head should be
        if not head: return head
        odd = head
        even = head.next
        even_head = head.next
        while even and even.next:
            # Notice: it is crutial to do odd first
            # if do even first, odd.next.next would have been updated
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        # after the while loop, odd is the tail of a linked list of all odd nodes
        # even is the tail of a linked list of all even nodes
        odd.next = even_head
        return head


