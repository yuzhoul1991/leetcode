# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # The root will be the smallest value in the tree
        root_val = root.val
        second_minimum = float('+inf')
        def traverse(node):
            nonlocal second_minimum
            if not node: return
            if node.val != root_val: 
                second_minimum = min(second_minimum, node.val)
                return
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        if second_minimum == float('+inf'): return -1
        return second_minimum
