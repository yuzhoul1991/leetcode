# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # Notice in postorder traversal, the last element is the root of the tree
        # locate the index of the root in the inorder array, then to the left of the element is the inorder traversal 
        # of the left subtree. same for right
        # with the size of inorder left and right, we know what the postorder array should pass to the recursive call

        idx_hsh = {k: v for v, k in enumerate(inorder)}
        # helper returns the root for the constructed subtree given the sub inorder and postorder arrays
        def helper(istart, iend, pstart, pend):
            if istart > iend or pstart > pend: return None
            root_val = postorder[pend]
            inorder_idx = idx_hsh[root_val]
            left_len = inorder_idx - istart
            right_len = iend - inorder_idx
            root = TreeNode(root_val)
            root.left = helper(istart, inorder_idx-1, pstart, pstart+left_len-1)
            root.right = helper(inorder_idx+1, iend, pend-right_len, pend-1)
            return root
        return helper(0, len(inorder)-1, 0, len(postorder)-1)
