# This programs makes it easier to put images into codeskulptor. It uses constants

import simplegui

SET = simplegui.load_image("http://2plunq3tkzat3cwrit1poghlzw7.wpengine.netdna-cdn.com/wp-content/uploads/sites/7/2014/08/THE-SIMPSONS-SEASON-21-014.jpg")

CARDWIDTH = SET.get_width()
CARDHEIGHT = SET.get_height()

DRAWSCALE =0.3
LOC_BACK_X = 430
LOC_BACK_Y = 250

def draw_handler(canvas):
    canvas.draw_image(SET, (CARDWIDTH / 2 , CARDHEIGHT / 2), 
                     (CARDWIDTH, CARDHEIGHT), 
                     (LOC_BACK_X, LOC_BACK_Y), 
                     (CARDWIDTH * DRAWSCALE, CARDHEIGHT * DRAWSCALE))

FRAMEWIDTH = 864
FRAMEHEIGHT = 600

frame = simplegui.create_frame('Testing', FRAMEWIDTH, FRAMEHEIGHT)
frame.set_draw_handler(draw_handler)
frame.start()
