class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        s_stack = []
        curr_s = []
        
        new_s = ""
        new_s += "1["
        new_s += s
        new_s += "]"
        
        i = 0
        while i < len(new_s):
            print("i: ", i)
            x = new_s[i]
            if x.isnumeric():
                j = i
                while x.isnumeric():
                    j += 1
                    x = new_s[j]
                    
                num_stack.append(new_s[i:j])
                s_stack.append(curr_s[:])
                curr_s = []
                i = j + 1
            elif x == "]":
                last_s = s_stack.pop(-1)
                last_num = num_stack.pop(-1)
                curr_s *= int(last_num)
                
                last_s += curr_s
                curr_s = last_s
                i += 1
                
            else:
                curr_s.append(x)
                i += 1
            print("x: ", x, "s_stack :", s_stack, "num_stack: ", num_stack, "curr_s: ", curr_s)    
        return "".join(curr_s)
                
            
                