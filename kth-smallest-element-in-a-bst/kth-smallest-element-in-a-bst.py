# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def search(root, answer):
            if root == None:
                return
            search(root.left, answer)
            answer.append(root.val)
            search(root.right, answer)
            
        answer = []
        search(root, answer)
        return answer[k - 1]
                
            
            
            
            