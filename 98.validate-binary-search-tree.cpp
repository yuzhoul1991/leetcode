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
    bool isValidBST(TreeNode* root) {
        // in a legal BST in order traversal should be ascending
        TreeNode *prev = NULL;
        return isValidBST(root, prev);
    }

private:
    // Notice need to pass pointer by ref here, otherwise change to prev won't take effect
    bool isValidBST(TreeNode* root, TreeNode* &prev) {
        if(root == NULL) return true;
        if(!isValidBST(root->left, prev)) return false;
        if(prev != NULL && prev->val >= root->val) return false;
        prev = root;
        return isValidBST(root->right, prev);
    }
};
