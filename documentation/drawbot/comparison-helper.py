# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
from drawBot import *
import math

# CONSTANTS
W = 1024  # Width
H = 512   # Height
M = 32    # Margin
U = 32    # Unit (Grid Unit)
F = 0     # Frames (Animation)

# DRAWS A GRID
def grid():
    strokeWidth(1)
    stroke(0,0,0.8)
    step_X = 0
    step_Y = 0
    increment_X = U
    increment_Y = U
    for x in range(32):
        polygon( (M+step_X, M), (M+step_X, H-M) )
        step_X += increment_X
    for y in range(16):
        polygon( (M, M+step_Y), (W-M, M+step_Y) )
        step_Y += increment_Y
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# NEW PAGE
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)

# SET FONT
font("../../fonts/ttf/BlueOcean.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))
varWght = 0
step = -1

# MAIN
new_page()
fontSize((M*0.5))
font("fonts/CascadiaCode.ttf")
#grid() # Toggle for grid view
fill(1)
stroke(None)
text("Blue Ocean Regular",(M*2, M*13))
text("Blue Ocean Bold",(M*2, M*10))
text("Blue Ocean Black",(M*2, M*7))
text("Bluu Next Bold",(M*2, M*4))
text("Bluu Suuperstar Regular",(M*17, M*13))
text("Bluu Suuperstar Bold",(M*17, M*10))
text("Bluu Suuperstar Black",(M*17, M*7))
text("Bluu Next Titling",(M*17, M*4))
image("reference/bluu-suuperstar-regular.png", (M*16.9, M*10.85))
image("reference/bluu-suuperstar-Bold.png", (M*16.9, M*7.85))
image("reference/bluu-suuperstar-Black.png", (M*16.9, M*4.85))

# COL 1
font("../../fonts/ttf/BlueOcean.ttf")
fontSize((M*2.5))
fontVariations(wght=400)
text("Blue Ocean", (M*2, M*11))

fontVariations(wght=700)
text("Blue Ocean", (M*2, M*8))

fontVariations(wght=900)
text("Blue Ocean", (M*2, M*5))

font("fonts/BluuNext-Bold.otf")
text("Blue Ocean", (M*2, M*2))

font("fonts/BluuNext-Titling.otf")
text("Blue Ocean", (M*17, M*2))

# SAVE THE OUTPUT IN THIS SCRIPT'S DIRECTORY LOCATION
saveImage("comparison-helper.gif")
