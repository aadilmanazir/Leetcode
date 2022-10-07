# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, arr):
            if root.left:
                dfs(root.left, arr)
            arr.append(root.val)
            if root.right:
                dfs(root.right, arr)
                
        arr = []
        dfs(root, arr)                
        curr = float('-inf')
        for x in arr:
            if x <= curr:
                return False
            curr = x
        return True
        
        
        
        