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
    int sumNumbers(TreeNode* root) {
        // iterative solution perform a preorder traversal 
        // while doing the traversal, keep track of the previous sum
        if(!root) return 0;
        stack<TreeNode*> node_stack;
        stack<int> prev_val_stack;
        node_stack.push(root);
        prev_val_stack.push(0);
        int ret = 0;
        while(!node_stack.empty()) {
            TreeNode* node = node_stack.top();
            node_stack.pop();
            int prev_val = prev_val_stack.top();
            prev_val_stack.pop();
            if(!node->left && !node->right) ret += node->val + 10*prev_val;
            if(node->left) {
                node_stack.push(node->left);
                prev_val_stack.push(node->val + 10*prev_val);
            }
            if(node->right) {
                node_stack.push(node->right);
                prev_val_stack.push(node->val + 10*prev_val);
            }
        }
        return ret;
    }
};
