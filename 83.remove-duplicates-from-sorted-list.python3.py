# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Since the linked list is sorted, we just iterate through it and 
        # only keep the first occurance
        if not head: return None
        seen = set()
        ptr = head
        while ptr:
            if ptr.val in seen:
                current = ptr
                while ptr and ptr.val == current.val:
                    ptr = ptr.next
                current.next = ptr
            else:
                seen.add(ptr.val)
        
        return head
