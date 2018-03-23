# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # easy recursive solution
        ret = []
        if not root: return []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        ret.extend(left)
        ret.extend(right)
        ret.append(root.val)
        return ret
        
