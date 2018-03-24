# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # inorder traversal of a BST is in ascending order
        # perform recursive inorder traversal and keep track of the count
        self.count = 0
        def inorder_traversal(root):
            if not root: return
            if root.left:
              inorder_traversal(root.left)
            self.count += 1
            if self.count == k: 
                self.ret = root.val
                return
            if root.right:
              inorder_traversal(root.right)
        inorder_traversal(root)
        return self.ret
        
