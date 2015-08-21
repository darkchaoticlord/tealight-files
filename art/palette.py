from tealight.art import (color, line, spot, rectangle, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)

stopMinY = 0
stopMaxY = 0
stopMinX = 0
stopMaxX = 0 


def stopButton():
  global stopMinY,stopMaxY,stopMinX,stopMaxX
  color("red")
  rectangle((screen_width - 180), screen_height - 40, 150,30)
  text(screen_width - 85, screen_height - 35, "STOP")
  stopMinX = (screen_width - 180)
  stopMaxX = (screen_width - 30)
  stopMinY = (screen_height - 40)
  stopMaxY = (screen_height - 10)
  print stopMinX

stopButton()






def finishButtons():
  global p2cMinX,p2cMaxX,p2cMinY,p2cMaxY, p2wMinX, p2wMaxX, p2wMinY, p2wMaxY, p3cMinX, p3cMaxX, p3cMinY, p3cMaxY, p3wMinX, p3wMaxX, p3wMinY, p3wMaxY
  color("green")
  #P2 Correct
  rectangle((screen_width / 2) - 75, screen_height / 2, 150,30)
  text((screen_width / 2) - 45, ((screen_height / 2) + 5), "P2 Correct")
  #P3 Correct
  rectangle((screen_width / 2) - 75, ((screen_height / 2) + 40), 150,30)
  text((screen_width / 2) - 45, ((screen_height / 2) + 45), "P3 Correct")
  
  color("red")
  #P2 Wrong
  rectangle((screen_width / 2) + 95, screen_height / 2, 150,30)
  text((screen_width / 2) + 125, ((screen_height / 2) + 5), "P2 Wrong")
  #P3 Wrong
  rectangle((screen_width / 2) + 95, ((screen_height / 2) + 40), 150,30)
  text((screen_width / 2) + 125, ((screen_height / 2) + 45), "P3 Wrong")
  
  p2cMinX = ((screen_width / 2) - 75)
  p2cMaxX = ((screen_width / 2) + 75)
  p2cMinY = (screen_height / 2)
  p2cMaxY = (screen_height / 2) + 30
  
  p2wMinX = ((screen_width / 2) + 95)
  p2wMaxX = ((screen_width / 2) + 245)
  p2wMinY = (screen_height / 2)
  p2wMaxY = ((screen_height / 2) + 30)
  
  p3cMinX = ((screen_width / 2) - 75)
  p3cMaxX = ((screen_width / 2) + 175) 
  p3cMinY = ((screen_height / 2) + 40)
  p3cMaxY = ((screen_width / 2) + 70)
  
  p3wMinX = ((screen_width / 2) + 95)
  p3wMaxX = ((screen_width / 2) + 245) 
  p3wMinY = ((screen_width / 2) + 40)
  p3wMaxY = ((screen_width / 2) + 70)









































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
  