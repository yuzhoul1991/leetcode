# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root, min_val, max_val):
            if not root: return True
            if root.val < min_val or root.val > max_val: return False
            return helper(root.left, min_val, root.val-1) and helper(root.right, root.val+1, max_val)
        if not root: return True
        return helper(root.left, float('-inf'), root.val-1) and helper(root.right, root.val+1, float('+inf'))
        
