# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
from drawBot import *
import math
#[W]IDTH,[H]EIGHT,[M]ARGIN,[F]RAMES
W,H,M,F = 2048,1024,64,64

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
    for y in range(12):
        polygon((M+M, (M+M)+stpY),
                (W-(M+M), (M+M)+stpY))
        stpY += incY

# NEW PAGE
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)

text_01 = '''
America needs to understand Islam, because this is the one religion that erases from its society the race problem. Throughout my travels in the Muslim world, I have met, talked to, and even eaten with people who in America would have been considered white, but the white attitude was removed from their minds by the religion of Islam. I have never before seen sincere and true brotherhood practiced by all together, irrespective of their color.”

—Malcolm X, Letter from Hajj
'''

new_page()
font("../../fonts/static/BlueOcean-Bold.ttf")
lineHeight(M)
#grid() # Toggle for grid view
stroke(None)
fill(1,1,1)
fontSize((M*0.7))
col_1_x = M*2
col_1_y = M*0
col_1_w = M*17
col_1_h = M*15

# Debug tools
fill(1,0,0)
#rect(col_1_x,col_1_y,col_1_w,col_1_h)
fill(1,1,1)

# Text
textBox(text_01, (col_1_x, col_1_y, col_1_w, col_1_h), align="left")
fontSize(M)
text("“",(M*1.5, M*13))
oval(M*29,M*2,M, M)
saveImage("quote-001.gif")
