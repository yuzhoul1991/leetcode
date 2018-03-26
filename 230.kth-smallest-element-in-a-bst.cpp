/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        // Use binary search
        // get the node cound of left child tree, if less than k, only search in right
        // subtree for k-left_count'th node
        int left_count = node_count(root->left);
        if(left_count == k-1) return root->val;
        else if(left_count >= k) 
            return kthSmallest(root->left, k);
        else
            // It is important to -1 here to account for root node
            return kthSmallest(root->right, k - 1 - left_count);
    }
private:
    int node_count(TreeNode* root) {
        if(!root) return 0;
        return 1 + node_count(root->left) + node_count(root->right);
    }
};
