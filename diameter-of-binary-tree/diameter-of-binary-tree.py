# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal res
            if node == None:
                return 0

            left = helper(node.left)
            right = helper(node.right)
            res = max(res, left + right + 1)
            return max(left + 1, right + 1)
        
        res = 0
        helper(root)
        return res-1
            
                