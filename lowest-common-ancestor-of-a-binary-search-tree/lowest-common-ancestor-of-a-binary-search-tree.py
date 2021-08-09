# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        r = root.val
        
        if root.val == p.val or root.val == q.val:
            return root
        
        if (p.val < r and q.val > r) or (p.val > r and q.val < r):
            return root
        
        if p.val < r and q.val < r:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        
        
        