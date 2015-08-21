from tealight.art import (color, line, spot, circle, box, image, text, background)
from math import floor
from tealight.art import (screen_width, screen_height)
from github.amyble.art.toolbar import *
from github.amyble.art.word import *
from github.amyble.art.correct import *
from tealight.net import connect, send
global stopCount


def inBox(boundXMin,boundXMax,boundYMin,boundYMax,x,y):
  if ((x > boundXMin) and (x < boundXMax)) and ((y > boundYMin) and (y < boundYMax)):
    return "true"
  else:
    return "false"
  




stopCount = "false"
connect("pictionary")

palette = ["red", "blue", "green", "purple", "yellow", "black", "pink", "grey"] 

global chosen_color
chosen_color = "red"
def reset():
  color("white")
  box(0, 0, screen_width, screen_height)
  color("black")

def initialPlayer1():
  reset()
  drawToolbar()
  text(10,10, "Colour Palette:")
  for i in range(0,8):
    color(palette[i])
    box((i * 25 + 10), 35, 25, 25)

  
#if (x < (len(palette)*25) and x > 10) and ((y > 35) and (y < 60)):    
#    chosen_colour = palette[int(floor((x-10)/25))]  
 
  
  
def getChosen(startX,startY,currentX,currentY,length):
  if (currentX < (length*25) and currentX > startX) and ((currentY > startY) and (currentY < (startY+25))):    
    return int(floor((currentX-startX)/25))
  else:
    return "no"
  
  
  
def handle_mousedown(x,y,button):
  # Check if clicking a colour on toolbar
  global chosen_color, p2cMinX, p2cMaxX, p2cMinY, p2cMaxY
  if getChosen(10,35,x,y,len(palette)) != "no":
    chosen_color = palette[getChosen(10,35,x,y,len(palette))]
  print chosen_color
  
  if inBox(p2cMinX,p2cMaxX,p2cMinY,p2cMaxY,x,y) == "true":
    print "p2c"
  
  global lastx, lasty
  lastx = x
  lasty = y


  
def handle_mousemove(x,y,button):
  global lastx, lasty
  if button == "left":
    color(chosen_color)
    line(lastx, lasty, x, y)
    send({"type": "line","x1": lastx, "y1": lasty, "x2": x, "y2": y,"color":chosen_color})
    lastx = x
    lasty = y
    
    
    
def handle_message(message):
  global stopCount
  if message["type"] == "stop":    
    reset()
    stopCount = "true"
    finishButtons()
    
  if message["type"] == "line":    
    color(message["color"])
    line(message["x1"], message["y1"], message["x2"], message["y2"])
  