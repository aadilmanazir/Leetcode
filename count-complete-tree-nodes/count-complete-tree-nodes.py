# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal count
            if node == None:
                return
            count += 1
            helper(node.left)
            helper(node.right)
        
        count = 0
        helper(root)
        return count
                
        