########################################
# Name: Sam Dyke
# Collaborators: Emma(Quad Center)
# Estimate time spent (hrs): 3ish hrs.
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score
color='red'
def clicky_box():


    
    def on_mouse_down(e):
    	x = e.get_x() #gets x pos of mouse
    	y = e.get_y() #gets y pos of mouse
    	bx= gw.box.get_x() #gets x pos of box.
    	by= gw.box.get_y() #gets y pos of box.

    	if x in range(int(bx),int(bx+SQUARE_SIZE)): #checks if mouse x pos is within square
    		if y in range(int(by),int(by+SQUARE_SIZE)): #checks if mouse y pos is within square.
    			gw.box.set_location(get_r(),get_r()) #moves box to new random location.
    			gw.score+=1 #adds 1 point to the score.
    			label() #runs label function
    		else:
    			gw.score-=gw.score #resets score when box y is missed.
    			label()
    	else:
    		gw.score-=gw.score #resets score when box x is missed.
    		label()
    	
    gw = GWindow(GW_WIDTH,GW_HEIGHT)
#    gw.box = GRect(225,225,50,50)
    gw.box = GRect(GW_WIDTH/2-SQUARE_SIZE/2,GW_HEIGHT/2-SQUARE_SIZE/2,SQUARE_SIZE,SQUARE_SIZE) 
#*** when above line is used, instead of gw.box = GRect(225,225,50,50), for some reason the 
#range functions from lines 27 and 28 require the numbers to become integers, but does not when I
#use commented out line 40, in other words, the int function isn't required if I use that.
    gw.box.set_filled(True)
    gw.box.set_color(color)
    gw.add(gw.box)
    gw.score=0 #sets score as 0 initially
    gw.label=GLabel(f"{gw.score}",SCORE_DX,GW_HEIGHT-SCORE_DY)
    gw.label.set_font(SCORE_FONT)
    gw.add(gw.label)
    def label(): #this function removes the previous label and replaces it with one displaying the new score.
    	gw.remove(gw.label)
    	gw.label=GLabel(f"{gw.score}",SCORE_DX,GW_HEIGHT-SCORE_DY)
    	gw.label.set_font(SCORE_FONT)
    	gw.add(gw.label)
    gw.add_event_listener("click",on_mouse_down)

def get_r():
    return random.randint(0, GW_HEIGHT-SQUARE_SIZE)









if __name__ == '__main__':
    clicky_box()
