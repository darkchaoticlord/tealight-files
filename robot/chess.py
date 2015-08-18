from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
while touch() == 'fruit':
  move()
for x in range(1,9):  
  if (x%2 != 0) and (right_side() == 'fruit'):
    turn(1)
    while right_side() != 'fruit':
      move()
    else:
      turn(1)
      while touch() == 'fruit':
        move()
  elif (x%2 == 0) and (left_side() == 'fruit'):
    turn(-1)
    while left_side() != 'fruit':
      move()
    else:
      turn(-1)
      while touch() == 'fruit':
        move()
turn(-1)
for x in range(0,32):
  move()