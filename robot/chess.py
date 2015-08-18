from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
for x in range(1,8):
  while touch() != None:
    move()
  if (x%2 != 0) and (right_side() == 'fruit'):
    turn(1)
    while right_side() != 'fruit':
      move()
    else:
      turn(1)
