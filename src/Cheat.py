from src.PlayingCard import PlayingCard
import os


class Cheat:
    Card = PlayingCard()

    def Main(self):
        self.pot = []
        self.last_played = []
        self.turn = 0
        self.players = self.get_players()
        self.deck = self.deal_deck(self.players)
        winner = None
        while winner == None:
            print(self.print_cards(self.deck, self.turn%self.players))
            cards = self.input_playcards()
            self.deck = self.remove_cards(self.deck, self.turn % self.players, cards)
            self.add_to_pot(cards)
            cheatcards = self.input_cheat_cards()
            self.is_cheat(cheatcards)
            winner = self.find_winner(self.deck)
            self.turn += 1



    def get_players(self):
        players = int(input('Number of player'))
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
        cards.append(card.upper())
        while card != '':
            card = input('What card(s) would you like to play: ')
            cards.append(card.upper())
        valid = self.validate_entry(self.deck, self.turn%self.players, cards)
        if valid == False:
            print('The cards must be in your hand')
            card = input('What card(s) would you like to play: ')
            cards = []
            cards.append(card.upper())
            while card != '':
                card = input('What card(s) would you like to play: ')
                cards.append(card.upper())
            valid = self.validate_entry(self.deck, self.turn % self.players, cards)
        return cards

    def validate_entry(self, deck, player, cards):
        valid = True
        for card in cards:
            if card not in deck[player]:
                if card != '':
                    valid = False
        return valid

    def remove_cards(self, deck, player, cards):
        for card in cards:
            if card != '':
                deck[player].remove(card)
        return deck

    def add_to_pot(self, cards):
        for i in range(0, len(cards)-1):
            self.pot.append(cards[i])
        self.last_played = cards[:-1]

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

    def is_cheat(self, cheatcards):
        cheat = input('Do you think it is cheat(Y/N): ')
        # asks first person for player number
        if cheat == 'Y':
            player = int(input('What player are you: '))
            is_cheat = self.validate_is_cheat(cheatcards, self.last_played)
            if is_cheat == False:
                self.deck[player] = self.add_cards(self.deck[player], self.pot)
            else:
                self.deck[self.turn % self.players] = self.add_cards(self.deck[self.turn % self.players], self.pot)
                self.turn = player - 1

    def validate_is_cheat(self, cards, last_played):
        is_cheat = False
        for card in last_played:
            if card[1:] in cards:
                cards.remove(card[1:])
            else:
                is_cheat = True
        return is_cheat

    def add_cards(self, hand, pot):
        for i in range(0, len(pot)):
            hand.append(pot[i])
        return hand

    def find_winner(self, hands):
        for i in range(len(hands)):
            if not hands[i]:
                return i

game = Cheat()
if __name__ == '__main__':
    game.Main()
