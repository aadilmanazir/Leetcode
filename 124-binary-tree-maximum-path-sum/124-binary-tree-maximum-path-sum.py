# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global curr_max
        curr_max = float('-inf')
        def helper(root):
            global curr_max
            if root.right:
                max_path_right = max(helper(root.right), 0)
            else:
                max_path_right = 0
                
            if root.left:
                max_path_left = max(helper(root.left), 0)
            else:
                max_path_left = 0
                
            curr_max = max(curr_max, root.val + max_path_left + max_path_right)
            res = max(root.val + max_path_left, root.val + max_path_right)
            return res
        
        helper(root)
        return curr_max
                