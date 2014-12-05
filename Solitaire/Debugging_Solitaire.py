# This program is being written to fix my bug in solitaire where only the spades do not show up. It will be as minimal as it
# can be

import simplegui

def definecards(deckstart, suit, setimg):
    global deck, ranks

    print suit
    
    for x in range(13):
        print deck[x + deckstart]
        print [x + deckstart]
        deck[x + deckstart] = Card("shuffled", suit, ranks[x], False, setimg, x)


spadesimg = simplegui.load_image("http://i.imgur.com/B0PojjI.png")

ranklen = 13
diamondsstart = 0 * ranklen
spadesstart = 1 * ranklen

diamondsimg = simplegui.load_image("http://i.imgur.com/rjCP3uF.png")
definecards(diamondsstart, 'Diamonds', diamondsimg)
spadesimg = simplegui.load_image("http://i.imgur.com/2FNx1am.png")
definecards(spadesstart, 'Spades', spadesimg)

