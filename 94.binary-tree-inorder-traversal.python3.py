# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # iterative solution
        # use a stack and push everything to stack until reaches left most node
        # push from stack and put node into ret
        # start from node.right go to step 1 again
        current = root
        stack = []
        ret = []
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop(-1)
                ret.append(current.val)
                current = current.right
        return ret
        
