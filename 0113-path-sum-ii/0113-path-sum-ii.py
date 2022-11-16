# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        def helper(arr, node, curr_sum, path):
            curr_sum += node.val
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    path.append(node.val)
                    arr.append(path)
                    
            if node.left:
                helper(arr, node.left, curr_sum, path[:] + [node.val])
                
            if node.right:
                helper(arr, node.right, curr_sum, path[:] + [node.val])
        arr = []        
        helper(arr, root, 0, [])
        return arr