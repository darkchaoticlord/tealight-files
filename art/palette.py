from tealight.art import (color, line, spot, circle, box, image, text, background)
from math import floor
from tealight.art import (screen_width, screen_height)
from github.amyble.art.toolbar import *


def colour_palette():
  global chosen_color
  color("white")
  box(0, 0, screen_width, screen_height)
  chosen_color = "red"
  color("black")
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
  global chosen_color
  if getChosen(10,35,x,y,len(palette)) != "no":
    chosen_color = palette[getChosen(10,35,x,y,len(palette))]
  print chosen_color
  
  global lastx, lasty
  lastx = x
  lasty = y
  
def handle_mousemove(x,y,button):
  global lastx, lasty
  if button == "left":

    color(chosen_color)
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
    
palette = ["red", "blue", "green", "purple", "yellow", "black", "pink", "grey"] 

colour_palette()