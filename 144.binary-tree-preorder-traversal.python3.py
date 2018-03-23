# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # iterative solution
        # use a stack
        # 1. push root to the stack
        # 2. pop from stack and add to the return list
        # 3. add right child to stack 
        # 4. add left child to stack 
        if not root: return []
        stack = [root]
        ret = []
        while stack:
            node = stack.pop(-1)
            ret.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return ret


        
