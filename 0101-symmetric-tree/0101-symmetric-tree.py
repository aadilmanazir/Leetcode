# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q1 = [root]
        q2 = [root]
        
        while q1 or q2:
            if not (q1 and q2):
                return False
            one = q1.pop(0)
            two = q2.pop(0)
            if not one and not two:
                continue
            if one == None and two or two == None and one or one.val != two.val:
                return False
            q1.append(one.left)
            q1.append(one.right)
            q2.append(two.right)
            q2.append(two.left)
            
        return True