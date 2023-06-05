/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int currMaxDepth;
    void helper(TreeNode* node, int currDepth) {
        if (node == nullptr) {
            return;
        }
        currMaxDepth = max(currMaxDepth, currDepth);
        helper(node->left, currDepth + 1);
        helper(node->right, currDepth + 1);
    }
    
    int maxDepth(TreeNode* root) {
        helper(root, 1);
        return currMaxDepth;
    }
};