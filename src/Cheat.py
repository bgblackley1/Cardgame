from src.PlayingCard import PlayingCard
import os


class Cheat:
    Card = PlayingCard()

    def Main(self):
        self.pot = []
        self.last_played = []

    def get_players(self):
        players = input('Number of player')
        return(players)

    def deal_deck(self, players):
        self.deck = self.Card.generate_deck()
        self.deck = self.Card.shuffle_cards(self.deck)
        self.cheatdeck = []
        for i in range(players):
            self.player = []
            for j in range(52//players):
                self.player.append(self.deck.pop())
            self.cheatdeck.append(self.player)
        return (self.cheatdeck)

    def print_cards(self, deck, player):
        return deck[player]

    def input_playcards(self):
        card = input('What card(s) would you like to play: ')
        cards = []
        cards.append(card)
        while card != '':
            card = input('What card(s) would you like to play: ')
            cards.append(card)
        return cards

    def validate_entry(self, deck, player, cards):
        valid = True
        for card in cards:
            if card not in deck[player]:
                valid = False
        return valid

    def remove_cards(self, deck, player, cards):
        for card in cards:
            deck[player].remove(card)
        return deck

    def add_to_pot(self, cards):
        self.pot.append(cards)
        self.last_played = cards

    def input_cheat_cards(self):
        print('dfg')
        for i in range(50):
            print()
        input('What card(s) have you played: ')

    def is

deck = Cheat()
deck.input_cheat_cards()