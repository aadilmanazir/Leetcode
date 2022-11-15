"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}
        visited = set()
        if node == None:
            return None
        def explore(node):
            if node == None:
                return
            visited.add(node.val)
            new_node = Node(node.val)
            d[node.val] = new_node
            for n in node.neighbors:
                if n.val not in visited:
                    explore(n)
                new_node.neighbors.append(d[n.val])
            
        explore(node)
        return d[1]
        