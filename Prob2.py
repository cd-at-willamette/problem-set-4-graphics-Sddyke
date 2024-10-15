########################################
# Name: Sam Dyke
# Collaborators: Olivia (Quad Center)
# Estimated time spent (hrs): 2 hrs.
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    basey=(HEIGHT/2)+(BRICKS_IN_BASE/2)*BRICK_HEIGHT - BRICK_HEIGHT
    g=0
    r=1
    cbrickcount = BRICKS_IN_BASE
    def e_row(cbrickcount,basex,basey,g,r):
    	print("placed brick")
    	for i in range(cbrickcount):
    		brick = GRect(BRICK_WIDTH,BRICK_HEIGHT)
    		gw.add(brick,basex,basey)
    		basex+=BRICK_WIDTH
#    		g+=40
    	basey-=BRICK_HEIGHT
    	r+=1
    	cbrickcount = cbrickcount-1
    	basex-= (cbrickcount+1)*BRICK_WIDTH
    	if cbrickcount != 0:
    		o_row(cbrickcount,basex,basey,g,r)
    	else:
    		return("done")
    
    def o_row(cbrickcount,basex,basey,g,r):
    	print("placed brick")
#    	basex-=basex
    	for i in range(cbrickcount):
    		brick = GRect(BRICK_WIDTH,BRICK_HEIGHT)
    		gw.add(brick,basex+BRICK_WIDTH/2,basey)
    		basex+=BRICK_WIDTH
#    		g+=40
    	basey-=BRICK_HEIGHT
    	r+=1
    	cbrickcount = cbrickcount-1
    	basex-= cbrickcount*BRICK_WIDTH
    	if cbrickcount != 0:
    		e_row(cbrickcount,basex,basey,g,r)
    	else:
    		return("done")
    gw = GWindow(WIDTH, HEIGHT)

    # You got it from here
    if cbrickcount % 2 == 0:
    	basex= WIDTH/2-(BRICKS_IN_BASE/2)*BRICK_WIDTH
    	e_row(cbrickcount,basex,basey,g,r)
    else:
    	basex= WIDTH/2-(BRICKS_IN_BASE/2)*BRICK_WIDTH - BRICK_WIDTH/2
    	o_row(cbrickcount,basex,basey,g,r)
    	
    
    	
	

















if __name__ == '__main__':
    draw_pyramid()

