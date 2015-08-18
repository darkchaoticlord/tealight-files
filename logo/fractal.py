from tealight.logo import move, turn

# Draws the von Koch Snowflake curve

def segment(scale, detail):
  
  if detail == 0:
    move(scale)
  else:
    segment(scale / 1.0, detail - 1)
    turn(-60)
    segment(scale / 1.0, detail - 1)
    turn(-60)
    segment(scale / 1.0, detail - 1)
    turn(-60)
    segment(scale / 1.0, detail - 1)
    

turn(90)
move(-300)
segment(600,3)
move(-300)