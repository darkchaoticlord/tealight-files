from tealight.logo import move, turn

# Draws the von Koch Snowflake curve

def triangle(size):
  turn(90)
  angle = 360.0 / 3
  for i in range(0, 3):
    move(size)
    turn(angle)
    
triangle(200)

def segment(scale, detail):
  
  if detail == 0:
    move(scale)
  else:
    segment(scale / 2.0, detail - 1)
    turn(-60)
    segment(scale / 2.0, detail - 1)
    turn(120)
    segment(scale / 2.0, detail - 1)
    turn(-60)
    segment(scale / 2.0, detail - 1)
    

turn(90)
move(-300)
segment(600,3)
move(-300)