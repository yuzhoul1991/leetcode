# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val == key:
            if not root.left: return root.right
            if not root.right: return root.left
            # find the min on the right sub tree
            ptr = root.right
            while ptr.left:
                ptr = ptr.left
            ptr.right = self.deleteNode(root.right, ptr.val)
            ptr.left = root.left
            root = ptr
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

        
