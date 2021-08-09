# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        answer = []
        q = [[root, 0]]
        while q != []:
            x = q.pop(0)
            tree = x[0]
            level = x[1]
            if level >= len(answer) or answer == []:
                answer.append([tree.val])
                
            else:
                answer[level].append(tree.val)
            
            if tree.left != None:
                q.append([tree.left, level + 1])
                
            if tree.right != None:
                q.append([tree.right, level + 1])        
        
        return answer
        