from tealight.art import (color, line, spot, circle, box, image, text, background)
from math import floor
from tealight.art import (screen_width, screen_height)

def colour_palette():
  text(10,10, "Colour Palette:")
  for i in range(0,8):
    color(palette[i])
    box((i * 25 + 10), 35, 25, 25)

palette = ["red", "blue", "green", "purple", "yellow", "black", "pink", "grey"] 
colour_palette()

#def colour_choose(x,y):

def handle_mousedown(x,y,b):
  if (x < (len(palette)*25) and x > 10) and ((y > 35) and (y <60)):    
    print int(floor((x-10)/25))