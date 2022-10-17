# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        temp = root
        num_cameras = 0
        def dfs(root):
            nonlocal num_cameras
            if root == None:
                return True, False
            # if root.left == None and root.right == None:
            #     return False, False
            
            left_fine, left_camera = dfs(root.left)
            right_fine, right_camera = dfs(root.right)
                
            if left_fine and right_fine and (left_camera or right_camera):
                return True, False
            elif left_fine and right_fine and not (left_camera or right_camera):
                if root != temp:
                    return False, False
                else:
                    num_cameras += 1
                    return True, True
            else:
                num_cameras += 1
                return True, True
            
        dfs(root)
        return num_cameras