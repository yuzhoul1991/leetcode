# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # reduce run time by testing the height of left and right
        # if they are equal, then it is a perfect BT, number of nodes is 2^d - 1
        # if not equal, use the traditional way
        if not root: return 0
        temp = root
        left_d = 0
        while temp:
            temp = temp.left
            left_d += 1
        temp = root
        right_d = 0
        while temp:
            temp = temp.right
            right_d += 1
        if left_d == right_d: return 2**left_d - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
