# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = [[root]]
        
        while queue:
            new = queue.pop(0)
            if new[-1] == p:
                p_ancestors = new
            if new[-1] == q:
                q_ancestors = new
                
            if new[-1].left is not None:
                queue.append(new + [new[-1].left])
            if new[-1].right is not None:
                queue.append(new + [new[-1].right])
        p_ancestors = set(p_ancestors)
        
        for ancestor in q_ancestors[::-1]:
            if ancestor in p_ancestors:
                return ancestor
        
        
        
        