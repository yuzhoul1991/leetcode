# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # naive solution: traverse the linked list and get all values
        # then compare the array
        if not head: return True
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]
        
