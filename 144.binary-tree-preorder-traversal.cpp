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
    vector<int> preorderTraversal(TreeNode* root) {
        // recursive solution       
        vector<int> ret;
        if(root) ret.push_back(root->val);
        else return {};
        vector<int> left_traverse = preorderTraversal(root->left);
        vector<int> right_traverse = preorderTraversal(root->right);
        ret.insert(ret.end(), left_traverse.begin(), left_traverse.end());
        ret.insert(ret.end(), right_traverse.begin(), right_traverse.end());
        return ret;
    }
};
