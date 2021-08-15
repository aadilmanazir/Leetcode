class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, x in enumerate(s):
            if x == '(':
                stack.append(('(', i))
            elif x == ')':
                if len(stack) == 0:
                    stack.append((')', i))
                elif stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((')', i))
        
        answer = ''
        ignore = set([x[1] for x in stack])
        for i in range(len(s)):
            if i not in ignore:
                answer += s[i]
                
        return answer
        
        
        
        
        
        
        