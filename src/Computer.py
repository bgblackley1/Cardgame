import src.Cheat
import random
from src.PlayingCard import PlayingCard


class Computer:

    def __init__(self, hand):
        self.hand = hand
        self.playingcard = PlayingCard

    def play_card(self, last_cards_played):
        self.playingcard.convert_faces_to_numbers(last_cards_played)
        self.playingcard.convert_faces_to_numbers(self.hand)
        above, below, equal = 0
        for card in self.hand:
            if int(card[1:]) == int(last_cards_played[0]) - 1:
                below += 1
            elif int(card[1:]) == int(last_cards_played[0]):
                below += 1
            elif int(card[1:]) == int(last_cards_played[0]) + 1:
                below += 1

        return actual, cheat

    def check_is_cheat(self, cards_played):
        pass
