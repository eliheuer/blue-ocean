# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com

from drawBot import *
import math

#[W]IDTH,[H]EIGHT,[M]ARGIN,[F]RAMES
W,H,M,F = 1024,1024,32,64

# DRAWS A GRID
def grid():
    stroke(0.2)
    strokeWidth(1)
    rect(M+M, M+M, W-(4*M), H-(4*M))
    stpX, stpY = 0, 0
    incX, incY = M, M
    for x in range(28):
        polygon(((M+M)+stpX, M+M),
                ((M+M)+stpX, H-(M+M)))
        stpX += incX
    for y in range(28):
        polygon((M+M, (M+M)+stpY),
                (W-(M+M), (M+M)+stpY))
        stpY += incY

# NEW PAGE
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)

new_page()

font("BlueOcean-Bold.ttf")
#grid() # Toggle for grid view
stroke(None)
fill(0.2,0,1)
fontSize((M*4))

text("Blue Ocean", (M*3, M*26))

fill(1)

fontSize((M*2.5))
text("Aa", (M*26, M*22))
text("Aa", (M*26, M*19))
text("Aa", (M*26, M*16))
text("Aa", (M*26, M*13))
text("Aa", (M*26, M*10))
text("Aa", (M*26, M*7))
text("Aa", (M*26, M*4))

text("ABCDEFGHIJKL", (M*3, M*22))
text("MNOPQRSTUVW", (M*3, M*19))
text("XYZ abcdefghijkl", (M*3, M*16))
text("mnopqrstuvwxy", (M*3, M*13))
text("z 1234567890 ßæ ", (M*3, M*10))
text("ÁÂÃÄÅàáâãäå", (M*3, M*7))
text("!@#$%&*():;,.", (M*3, M*4))

saveImage("basic-specimen.png")
