class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        l = []
        for i, c in enumerate(costs):
            l.append([abs(c[0] - c[1]), i])
        
        l.sort(key = lambda x: x[0], reverse = True)
        
        A = 0
        B = 0
        res = 0
        
        for i in range(len(l)):
            person = l[i]
            index = person[1]
            
            if A == len(costs)//2:
                B += 1
                res += costs[index][1]
                continue
            elif B == len(costs)//2:
                A += 1
                res += costs[index][0]
                continue
                
            if costs[index][0] < costs[index][1]:
                A += 1
                res += costs[index][0]
            else:
                B += 1
                res += costs[index][1]
                
        return res