class Flop:
    # Class for flop
    def __init__(self, flop_cards: list, action_stream: list):
        self.flop_cards = flop_cards
        self.action_stream = action_stream

class Turn:
    # Class for turn
    def __init__(self, turn_card: Card):
        return

class River:
    # Class for river
    def __init__(self, river_card: Card):
        return

class Card:
    # Class for a poker card
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

class Player:
    def __init__(self, player_id, stack_size):
        self.id = player_id
        self.stack = stack_size