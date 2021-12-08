from src.PlayingCard import PlayingCard
from Computer import Computer_Player
import os


class Cheat:
    Card = PlayingCard()

    def __init__(self):
        self.players = self.get_players()
        self.computers = self.set_computer_players()
        self.turn = 0
        self.last_played = []
        self.pot = []
        self.computer_players = [None] * (self.players - self.computers)
        self.computer_or_player = ['p'] * (self.players - self.computers)
        self.Main()

    def Main(self):
        self.deck = self.deal_deck(self.players)
        for i in range(self.computers):
            self.computer_or_player.append('c')
            self.computer_players.append(Computer_Player(self.deck[self.players - self.computers + i]))
        winner = None
        while winner == None:
            if self.computer_or_player[self.turn%self.players] == 'p':
                print(self.print_cards(self.deck, self.turn%self.players))
                cards = self.input_playcards()
                self.deck = self.remove_cards(self.deck, self.turn % self.players, cards)
                self.add_to_pot(cards)
                cheatcards = self.input_cheat_cards()
                self.is_cheat(cheatcards)
            else:
                comp_cards = self.computer_players[self.turn%self.players].play_card(self.last_played)
                self.deck = self.remove_cards(self.deck, self.turn % self.players, comp_cards[0])
                print('The computer played: ', ', '.join(comp_cards[1]))
                self.add_to_pot(comp_cards[0])
                self.is_cheat(comp_cards[1])
            winner = self.find_winner(self.deck)
            self.turn += 1

    def get_players(self):
        players = int(input('Number of players: '))
        return (players)

    def set_computer_players(self):
        computers = int(input('Number of computers: '))
        return computers

    def deal_deck(self, players):
        self.deck = self.Card.generate_deck()
        self.Card.convert_faces_to_numbers(self.deck)
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
        self.last_played = []
        for card in cards:
            if card != '':
                self.pot.append(card)
                self.last_played.append(card)

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
        cheatcalled = False
        # asks first person for player number
        while cheatcalled == False:
            for i in range(self.players):
                if i != self.turn% self.players:
                    for j in range(50):
                        print()
                    print(cheatcards)
                    print(self.deck[i])
                    cheat = input('Player', i,  'do you think it is cheat(Y/N): ')
                    if cheat == 'Y':
                        cheatcalled = True
                        player = int(input('What player are you: '))
                        is_cheat = self.validate_is_cheat(cheatcards, self.last_played)
                        if is_cheat == False:
                            self.deck[player] = self.add_cards(self.deck[player], self.pot)
                        else:
                            self.deck[self.turn % self.players] = self.add_cards(self.deck[self.turn % self.players], self.pot)
                            self.turn = player - 1
        if cheatcalled == False:
            for i in range((self.players - self.computers), len(self.computer_players)):
                cheat = self.computer_players[i].check_is_cheat(cheatcards)
                if cheat == True:
                    self.deck[self.turn % self.players] = self.add_cards(self.deck[self.turn % self.players], self.pot)
                    print('the computer called cheat')
                    self.turn = self.players + i - 1


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
