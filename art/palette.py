from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

def colour_palette():
  for i in range(0,7):
    color(palette[i])
    box((i * 25 + 10), (10), 25, 25)

palette = ["red", "blue", "green", "purple", "yellow", "black", "pink", "grey"] 
colour_palette()