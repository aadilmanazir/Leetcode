# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root, col, row, d):
            if root == None:
                return
            if col not in d:
                d[col] = [[root.val, row]]
            else:
                d[col].append([root.val, row])
                
            helper(root.left, col-1, row + 1, d)
            helper(root.right, col + 1, row + 1, d)
            
            return
        
        d = {}
        helper(root, 0, 0, d)
        keys = list(d.keys())
        keys.sort()
        res = []
        for k in keys: 
            d[k].sort(key = lambda x: [x[1], x[0]])
            res.append([x[0] for x in d[k]])
            
        return res
        
        
        
        