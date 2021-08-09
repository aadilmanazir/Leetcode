# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def same(r1, r2):
            if r1 == None and r2 == None:
                return True
            elif r1 == None or r2 == None:
                return False
            
            return r1.val == r2.val and same(r1.left, r2.left) and same(r1.right, r2.right)
        
        if subRoot == None:
            return True
        
        elif root == None:
            return False
        
        if same(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        
        
        
        
        
        
        
        
        
        
        