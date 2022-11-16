# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, row, col):
            if not node:
                return
            if col not in d:
                d[col] = []
            d[col].append([node.val, row])
            helper(node.left, row + 1, col - 1)
            helper(node.right, row + 1, col + 1)
             
        d = {}
        helper(root, 0, 0)
        res = []
        for col in sorted(d.keys()):
            d[col].sort(key = lambda x: x[1])
            res.append([x[0] for x in d[col]])
                
        return res