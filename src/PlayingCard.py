import random

class PlayingCard:
    suits = {"H": "Hearts", "D": "Diamonds", "S": "Spades", "C": "Clubs"}
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    user_hand = 0

    # Function: generate_deck
    # Description: This function generates a 52 pack of cards, with four suites and 13 playing cards Ace to King.
    # The cards are returned in an ordered deck
    def generate_deck(self):
        deck = []
        for suit in self.suits.keys():
            for face in self.faces:
                deck.append(suit + face)
        return deck

    # Function: shuffle_deck
    # Description: A set of cards is supplied and shuffled, randomly ordered.
    def shuffle_cards(self,cards):
        random.shuffle(cards)
        return cards

    # Method: trentine_small
    # Description: An Italian set of cards Tertine can be only 40 cards or 52. The small set has no "8", "9" or "10". It
    # still has ace to seven and jack, queen and king.
    def trentine_small(self, cards):
        for card in cards:
            faces = card[1:len(card)]
            if faces == 8 or 9 or 10:
                cards.remove(card)

    # Function: deal_a_card
    # Description: Remove a card from a deck or hand of cards and return the card.
    def deal_a_card(self,cards):
        return cards.pop()

    # Function: deal_cards
    # Description: Deal a number of cards from a deck to a number of players (no of hands). Optionally an existing set of
    # hands of cards can be passed. The default is for no existing hands of cards to be passed.
    def deal_cards(self,deck, no_of_cards, no_of_hands):
        hands=[]
        all_cards = False
        if no_of_cards == 0:
            no_of_cards = int(len(deck)/no_of_hands) - 1
            all_cards = True

        for index in range(0, no_of_hands):
            hands += [[]]

        for hand_index in range(0, no_of_hands):
            while len(hands[hand_index]) < no_of_cards and len(deck) > 0:
                dealt_card = self.deal_a_card(deck)
                hands[hand_index].append(dealt_card)

        if all_cards:
            counter = 0
            while len(deck) > 0:
                hands[counter].append(self.deal_a_card(deck))
                counter = (counter +1) % no_of_hands

        return hands

    # Method: play_a_card
    # Description: A hand of cards is input and an individual playing card. If the individual playing card is found in the hand it is removed from
    # the hand.
    def play_a_card(self, hand, card_to_play):
        if card_to_play in hand:
            hand.remove(card_to_play)

    # Function: is_playing_a_card
    # Description: For a given hand of cards if an individual hand of card is found it is removed from the hand and returns
    # True if no card if found this function returns False.
    def is_playing_a_card(self, hand, card_to_play):
        played = False
        current_size = len(hand)
        self.play_a_card(hand, card_to_play)
        if current_size > len(hand):
            played = True
        return played

    # Function: convert_face_to_name
    # Description: An individual playing card is input and it is a face card e.g. A, K, Q, J we convert to hexadecimal. We
    # include converting a 10 to A, since it will order 1, 2, ...9, A, B, C, D. The converted individual playing card is returned.
    # HA -> H1
    # H10 -> H10 -- No change
    # HJ -> H11
    # HQ -> H12
    # CK -> C13
    def convert_face_to_number(self, card):
        face = card[1:len(card)]
        if face == "K":
            new_face = "13"
        elif face == "Q":
            new_face = "12"
        elif face == "J":
            new_face = "11"
        elif face == "10":
            new_face = "10"
        elif face == "A":
            new_face = "01"
        else:
            new_face = str(0) + face

        return card[0] + new_face

    # Method: convert_faces_to_numbers
    # Description: For a hand of cards, each playing card in the hand is converted from faces to hexadecimal numbers
    def convert_faces_to_numbers(self, hand):
        for counter in range(0, len(hand)):
            hand[counter] = self.convert_face_to_number(hand[counter])

    # Function: convert_number_to_face
    # Description: For an individual playing card this reverse the conversion from Face to hexadecimal number.
    def convert_number_to_face(self, card):
        face = card[1:len(card)]
        if face == "13":
            new_face = "K"
        elif face == "12":
            new_face = "Q"
        elif face == "11":
            new_face = "J"
        elif face == "10":
            new_face = "10"
        elif face == "01":
            new_face = "A"
        else:
            new_face = str(int(face))
        return card[0] + new_face

    # Method: convert_numbers_to_faces
    # Description: For a hand of cards, each playing card in the hand is converted from a hexadecimal number to a face card
    def convert_numbers_to_faces(self, hand):
        for counter in range(0, len(hand)):
            hand[counter] = self.convert_number_to_face(hand[counter])

    # Method: sort_hand
    # Description: For a hand of playing cards it is sorted. It is converted to hexadecimal numbers, sorted and converted
    # back to face cards
    def sort_hand(self, hand):
        self.convert_faces_to_numbers(hand)
        hand.sort()
        self.convert_numbers_to_faces(hand)

    # Method: sort_hands
    # Description: For a set of hands of cards for a number of players, each hand is sorted
    def sort_hands(self, hands):
        for hand in hands:
            self.sort_hand(hand)
