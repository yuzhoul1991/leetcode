# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # recursive solution 
        # current running sum = 10 * previous + node.val
        def get_sum(node, previous):
            if not node: return 0
            if not node.left and not node.right: return node.val + 10 * previous
            return get_sum(node.left, node.val + 10*previous) + get_sum(node.right, node.val + 10*previous)
        return get_sum(root, 0)
