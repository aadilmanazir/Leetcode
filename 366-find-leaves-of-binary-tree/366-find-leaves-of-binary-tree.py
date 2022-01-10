# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root, array):
            if root == None:
                return None
            
            if root.left == None and root.right == None:
                array.append(root.val)
                return None
            
            root.left = helper(root.left, array)
            root.right = helper(root.right, array)
            return root
        
        leaves = []
        while root != None:
            new_leaf = []
            root = helper(root, new_leaf)
            leaves.append(new_leaf)
    
        return leaves