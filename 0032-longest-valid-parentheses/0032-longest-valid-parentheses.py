class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        
        for i, x in enumerate(s):
            if x == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)

                res = max(res, i - stack[-1])
                    
        return res