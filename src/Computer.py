import random
from src.PlayingCard import PlayingCard


class Computer_Player:

    def __init__(self, hand):
        self.hand = hand
        self.playingcard = PlayingCard()
        self.above, self.below, self.equal = [0], [0], [0]

    def play_card(self, last_cards_played):
        self.above, self.below, self.equal = [0], [0], [0]
        self.last_cards_played = last_cards_played
        for card in self.hand:
            if int(card[1:]) == int(last_cards_played[0][1:]) - 1:
                self.below[0] += 1
                self.below.append(card)
            elif int(card[1:]) == int(last_cards_played[0][1:]):
                self.equal[0] += 1
                self.equal.append(card)
            elif int(card[1:]) == int(last_cards_played[0][1:]) + 1:
                self.above[0] += 1
                self.above.append(card)
        return self.check_can_play()

    def check_can_play(self):
        cards = [self.below[0], self.equal[0], self.above[0]]
        cards.sort()
        if cards[2] != 0:
            if cards[2] == self.below[0]:
                played = self.below[1:]
                said = [self.below[1][1:]] * self.below[0]
                cardsreturn = [played, said]
                return cardsreturn
            elif cards[2] == self.equal[0]:
                played = self.equal[1:]
                said = [self.equal[1][1:]] * self.equal[0]
                cardsreturn = [played, said]
                return cardsreturn
            elif cards[2] == self.above[0]:
                played = self.above[1:]
                said = [self.above[1][1:]] * self.above[0]
                cardsreturn = [played, said]
                return cardsreturn
        else:
            self.must_cheat()

    def must_cheat(self):

        if len(self.hand) >= 4:
            playing = random.randint(1, 4)
        else:
            playing = random.randint(1, len(self.hand))
        value = random.randint(-1, 1)
        cards = []
        for i in range(playing):
            cards.append(self.hand[random.randint(0, len(self.hand) - 1)])
        cards_said = [self.last_cards_played[0] + value] * playing
        return cards, cards_said

    def check_is_cheat(self, last_cards_played):
        num_cards = 0
        for card in self.hand:
            if int((card[1:])) == int((last_cards_played[0])):
                num_cards += 1
        if num_cards + len(last_cards_played) - 1 > 4:
            return True
        else:
            return False

