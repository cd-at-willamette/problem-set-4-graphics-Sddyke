############################################################
# Name: Sam Dyke
# Name(s) of anyone worked with:
# Est time spent (hr): 1hr
# Description: This generates the word "Life" written in a fictional language where every circle is a character
# and the pattern within the circle corresponds to a specific character in the English alphabet.
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600
w=150
l=150
def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    
    # Creates 4 large, unfilled circles, and 1 small filled circle.
    #NOTE: Ideally, the 4 large circles would have been hexagons with the same patterns inside, however that would have taken a lot...
    #... more tedious work of either making the hexagons with a bunch of lines, or I'd need to learn how to use the polygon commands.
    c1 = GOval(0,225,w,l)
    c1.set_color("#32CD32")
    gw.add(c1)
    c2 = GOval(150,225,w,l)
    c2.set_color("#32CD32")
    gw.add(c2)
    c3 = GOval(300,225,w,l)
    c3.set_color("#32CD32")
    gw.add(c3)
    c4 = GOval(450,225,w,l)
    c4.set_color("#32CD32")
    gw.add(c4)
    c5 = GOval(405,330,5,5)
    c5.set_color("#32CD32")
    c5.set_filled(True)
    gw.add(c5)
    
    # Creates the patterns found within the circles, these are not exactly in the correct order, will comment which is which accordingly.
    
    # 3rd circle pattern:
    l1=GLine(300,300,w,w/2)
    l1.set_start_point(300,300)
    l1.set_end_point(450,300)
    l1.set_color("#32CD32")
    gw.add(l1)
    l2=GLine(300,300,w,w/2)
    l2.set_start_point(375,300)
    l2.set_end_point(375,375)
    l2.set_color("#32CD32")
    # 1st circle pattern:
    gw.add(l2)
    l3=GLine(0,0,w,w/2)
    l3.set_start_point(40,233)
    l3.set_end_point(40,367)
    l3.set_color("#32CD32")
    gw.add(l3)
    l4=GLine(0,0,w,w/2)
    l4.set_start_point(110,233)
    l4.set_end_point(110,367)
    l4.set_color("#32CD32")
    gw.add(l4)
    # 2nd circle pattern:
    l5=GLine(0,0,w,w/2)
    l5.set_start_point(180,360)
    l5.set_end_point(225,310)
    l5.set_color("#32CD32")
    gw.add(l5)
    l6=GLine(300,300,w,w/2)
    l6.set_start_point(225,310)
    l6.set_end_point(225,290)
    l6.set_color("#32CD32")
    gw.add(l6)
    l7=GLine(0,0,w,w/2)
    l7.set_start_point(225,290)
    l7.set_end_point(270,240)
    l7.set_color("#32CD32")
    gw.add(l7)





if __name__ == '__main__':
    draw_image()
