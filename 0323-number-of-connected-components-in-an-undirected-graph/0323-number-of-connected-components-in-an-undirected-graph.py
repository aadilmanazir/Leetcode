class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        d = {}
        for i in range(n):
            d[i] = []
            
        for e in edges:
            u, v = e
            d[u].append(v)
            d[v].append(u)
                
        def explore(v):
            visited.add(v)
            for u in d[v]:
                if u not in visited:
                    explore(u)
        res = 0            
        for i in range(n):
            if i not in visited:
                explore(i)
                res += 1
                
        return res
            