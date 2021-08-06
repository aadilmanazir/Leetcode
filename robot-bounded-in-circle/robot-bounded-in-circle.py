class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def direction(curr, rotate):
            if rotate == 'L':
                if curr == 'n':
                    return 'w'
                elif curr == 'e':
                    return 'n'
                elif curr == 's':
                    return 'e'
                else:
                    return 's'
            else:
                if curr == 'n':
                    return 'e'
                elif curr == 'e':
                    return 's'
                elif curr == 's':
                    return 'w'
                else:
                    return 'n'
                
        def move(curr, pos):
            if curr == 'n':
                pos[1] += 1
            elif curr == 'e':
                pos[0] += 1
            elif curr == 's':
                pos[1] -= 1
            else:
                pos[0] -= 1
                
        curr = 'n'
        pos = [0, 0]
        for x in instructions:
            if x == 'G':
                move(curr, pos)
                
            else:
                curr = direction(curr, x)
                
        if pos != [0, 0] and curr == 'n':
            return False
        return True
                
        
        
        
        
        
        
        