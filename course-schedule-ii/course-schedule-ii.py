class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = {}
        for n in range(numCourses):
            g[n] = []
            
        for p in prerequisites:
            a = p[0]
            b = p[1]
            
            g[b].append(a)
        
        seen = set()
        pre = {}
        post = {}
        clock = 0
        
        def explore(g, u, pre, post):
            nonlocal clock
            if u in seen:
                return
            seen.add(u)
            
            clock += 1
            pre[u] = clock
            
            for v in g[u]:
                explore(g, v, pre, post)
                
            clock += 1

            post[u] = clock
            
        for u in g:
            explore(g, u, pre, post)
        
        for u in g:
            for v in g[u]:
                if pre[v] < pre[u] and pre[u] < post[u] and post[u] < post[v]:
                    return []
                
        l = []
        for u in post:
            l.append((u, post[u]))
            
        return [x[0] for x in sorted(l, key = lambda x: x[1], reverse=True)]