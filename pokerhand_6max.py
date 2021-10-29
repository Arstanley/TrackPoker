from base_classes import *

class WholeHand:
    # Class for a whole hand, including actions on multiple streets
    def __init__(self, players, button_position, hand, card, position, streets):
        self.players = players
        self.button_position = button_position        
        self.hand1 = hand[0]
        self.hand2 = hand[1]
        

