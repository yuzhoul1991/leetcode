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
    int findSecondMinimumValue(TreeNode* root) {
        //iterative solution
        // do level order tree traversal and pruning
        queue<TreeNode*> queue;
        queue.push(root);
        int min_val = root->val;
        int second_min = INT_MAX;
        while(!queue.empty()) {
            TreeNode* node = queue.front();
            queue.pop();
            if(node->val > min_val && node->val < second_min) {
                second_min = node->val;
                // if node->val is the new second_min, then no need to look at it's subtrees
            }
            else {
                if(node->left)  queue.push(node->left);
                if(node->right)  queue.push(node->right);
            }
        }
        return second_min == INT_MAX ? -1 : second_min;
    }
};
