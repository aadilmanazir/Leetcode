# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        self.done = False
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if self.done:
                return
            
            if root == None:
                return [False, False]
            
            seen_left = helper(root.left, p, q)
            seen_right = helper(root.right, p, q)
                
            seen_p = root == p or seen_left[0] or seen_right[0]
            seen_q = root == q or seen_left[1] or seen_right[1]
            
            if seen_p and seen_q and not self.done:
                self.ans = root
                self.done = True

            return [seen_p, seen_q]
            
        helper(root, p, q)
        return self.ans