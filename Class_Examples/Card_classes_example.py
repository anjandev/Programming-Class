# Card Class Example

class Card:
    
    # Initializer
    def __init__(self, image, suit, rank, position, exposed):
    	self.image = image
        self.suit = suit
        self.rank = rank
        self.position = position
        self.exposed = exposed
    
	# Returns a string for the print function    
    def __str__(self):
        return self.rank + "of" + self.suit + "at position" + str(self.position)
    
    # Getters
    def get_image(self):
        return self.image
    
    def get_suit(self):
        return self.suit
    
    #...
    
    # Setters
    def exposed(self):
        self.exposed = True
        
    def exposed(self):
        self.exposed = False
    
    # Seperate Draw Method
    def draw_card(self, canvas):
        if self.exposed:
            canvas.draw_image(...)
    	else:
            canvas.draw_polygon(...)
