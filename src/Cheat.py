from src.PlayingCard import PlayingCard
import os


class Cheat:
    Card = PlayingCard()

    def Main(self):
        self.pot = []
        self.last_played = []
        self.turn = 0
        self.players = self.get_players()
        self.deck = self.deal_deck()
        winner = None


    def get_players(self):
        players = input('Number of player')
        return (players)

    def deal_deck(self, players):
        self.deck = self.Card.generate_deck()
        self.deck = self.Card.shuffle_cards(self.deck)
        self.cheatdeck = []
        for i in range(players):
            self.player = []
            for j in range(52 // players):
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
        for i in range(50):
            print()
        card = input('What card(s) have you played: ')
        cards = []
        cards.append(card)
        while card != '':
            card = input('What card(s) have you played: ')
            cards.append(card)
        return cards

    def is_cheat(self):
        cheat = input('Do you think it is cheat(Y/N): ')
        # asks first person for player number
        player = input('What player are you: ')
        if cheat == 'Y':
            is_cheat = self.validate_is_cheat(self.input_cheat_cards(), self.last_played)
            if is_cheat == False:
                self.deck[player] = self.add_cards(self.deck[player], self.pot)
            else:
                self.deck[self.turn % self.players] = self.add_cards(self.deck[self.turn % self.players], self.pot)

    def validate_is_cheat(self, cards, last_played):
        is_cheat = False
        for card in last_played:
            if card[1:] in cards:
                cards.remove(card[1])
            else:
                is_cheat = True
        return is_cheat

    def add_cards(self, hand, pot):
        pot += hand
        return pot

    def find_winner(self,hands):
        for i in range(len(hands)):
            if not hands[i]:
                return i
