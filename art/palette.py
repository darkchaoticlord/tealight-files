from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

def colour_palette():
  text(10,10, "Colour Palette:")
  for i in range(0,8):
    color(palette[i])
    box((i * 25 + 10), 35, 25, 25)

palette = ["red", "blue", "green", "purple", "yellow", "black", "pink", "grey"] 
colour_palette()

#def colour_choose(x,y):
print float(34/25)