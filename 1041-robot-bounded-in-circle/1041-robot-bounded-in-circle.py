class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        TURNS = {'n': ('w', 'e'), 'e': ('n', 's'), 's': ('e', 'w'), 'w': ('s', 'n')}
        x, y = 0, 0
        direction = 'n'
        for inst in instructions:
            if inst == 'G':
                if direction == 'n': 
                    y += 1
                elif direction == 'e':
                    x += 1
                elif direction == 's':
                    y -= 1
                elif direction == 'w':
                    x -=1
            elif inst == 'L':
                direction = TURNS[direction][0]
            elif inst == 'R':
                direction = TURNS[direction][1]
        
        if x == 0 and y == 0:
            return True
        return direction != 'n'
        
        
        