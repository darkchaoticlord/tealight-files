from tealight.art import (color, line, spot, circle, box, image, text, background)
from math import floor
from tealight.art import (screen_width, screen_height)
from github.amyble.art.toolbar import *
from github.amyble.art.word import *
from tealight.net import connect, send

connect("pictionary")

global chosen_color
chosen_color = "red"

def initialPlayer2():
  color("white")
  box(0, 0, screen_width, screen_height)
  color("black")

  
#if (x < (len(palette)*25) and x > 10) and ((y > 35) and (y < 60)):    
#    chosen_colour = palette[int(floor((x-10)/25))]  
 
  
  
def getChosen(startX,startY,currentX,currentY,length):
  if (currentX < (length*25) and currentX > startX) and ((currentY > startY) and (currentY < (startY+25))):    
    return int(floor((currentX-startX)/25))
  else:
    return "no"
  
  
  
def handle_mousedown(x,y,button):


  

def handle_message(message):
  if message["type"] == "line":    
    color(message["color"])
    line(message["x1"], message["y1"], message["x2"], message["y2"])
  