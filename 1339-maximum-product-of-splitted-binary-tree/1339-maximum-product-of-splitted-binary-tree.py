# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = set()
        def helper(root):
            nonlocal curr_max
            if root == None:
                return 0
            
            left_sum = helper(root.left)
            right_sum = helper(root.right)
            new_sum = root.val + left_sum + right_sum
            
            sums.add(new_sum)
            
            return new_sum
        root_sum = helper(root)
        curr_max = float('-inf')
        for x in sums:
            curr_max = max(curr_max, (root_sum - x) * x)
        return int(curr_max % (1e9 + 7))
            