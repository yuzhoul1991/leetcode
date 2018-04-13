# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

         two pointer chasing solution
         L1 is head to entry distance
         L2 is entry to meeting point distance
         C is the length of the loop
         When the two pointers meet, slow pointer traveled L1 + L2
         fast pointer traveled L1 + L2 + n * C
         Since faster pointer is twice as speedy as slow pointer => 2(L1 + L2) = L1 + L2 + n*C
         L1 = (n-1)C + (C-L2) where C-L2 is from meeting point to entry point distance. ie. how much to travel
         to get from meeting point to the entry point
         Since it is a cycle remove the (n-1)C term we have L1 = C - L2
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # Now two pointer meet
            if slow == fast: 
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return slow
        return None

        
