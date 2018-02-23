class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # The same way of basic two sum, traverse the tree and keep updating a hash
        seen = set()
        def helper(root, k):
            if not root: return False
            if k - root.val in seen: return True
            seen.add(root.val)
            return helper(root.left, k) or helper(root.right, k)
        return helper(root, k)
