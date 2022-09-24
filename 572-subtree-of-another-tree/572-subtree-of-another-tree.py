# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def helper(root, subRoot, equal):
            if root is None and subRoot is not None:
                return False
            elif subRoot is None and root is not None:
                return False
            elif root == None and subRoot == None:
                return True

            if root.val == subRoot.val:
                if helper(root.right, subRoot.right, True) and helper(root.left, subRoot.left, True):
                    return True
            if not equal:
                return helper(root.right, subRoot, False) or helper(root.left, subRoot, False)
            return False


        return helper(root, subRoot, False)
        
        
        
        
        
        
        
        