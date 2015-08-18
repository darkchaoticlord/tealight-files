from tealight.logo import move, turn

def square(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)

for x in range(0,8):
  for y in range(0,8):    
     square(4,25)
     move(25)
  if x%2 != 0:
    turn(180)
  else:
    turn(-180)