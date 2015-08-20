from tealight.logo import move, turn

def square(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)

def fill_in(

for x in range(0,8):
  for y in range(0,8):    
     square(4,25)
     move(25)
  move(-200)
  turn(90)
  move(25)
  turn(-90)
  
