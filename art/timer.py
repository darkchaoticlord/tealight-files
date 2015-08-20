from tealight.utils import now
from tealight.art import text,box,color, background, screen_width, screen_height

startTime = now()
i=0
global points
points = 31

def doSecond(): 
  global points
  points = points-1
  color("white")
  box(screen_width - 100,screen_height - 100, 100, 100)
  color("black")
  text(10,screen_height - 30, ("Points: " + str(points)))

def handle_frame():
  global i
  if (i % 60) == 0:
    newTime = now() - startTime
    doSecond()
  
  # Do everything else on framechange

  i=i+1
