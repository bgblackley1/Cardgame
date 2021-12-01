import random
from src.PlayingCard import PlayingCard


class BlackJack:
    """Constant values to be references in the functions and methods below."""
    winning_score = 21
    face_card_score = 10
    max_ace_score = 11
    min_ace_score = 1
    good_number_of_cards = 5

    playing_card = PlayingCard()

    def score_hand(self, hand):
        """Score an individual hand of playing cards. We add each card score to a total. All face cards King, Queen
     and Jack score ten. If the hand has an ace we can score at one or eleven. If the hand is less than or equal to eleven
     then ten additional score is added on (one already been added and the score for the ace is eleven)"""
        total_score = 0
        has_an_ace = False
        self.playing_card.convert_faces_to_numbers(hand)
        for card in hand:
            if int(card[1:len(card)]) == self.min_ace_score:
                has_an_ace = True
            if int(card[1:len(card)]) > self.face_card_score:  # Face cards i.e. King, Queen and Jack
                total_score += self.face_card_score
            else:
                total_score += int(card[1:len(card)])
        self.playing_card.convert_numbers_to_faces(hand)
        if total_score > self.winning_score:
            total_score = 0
        elif has_an_ace and total_score <= self.max_ace_score:
            total_score += self.max_ace_score - self.min_ace_score

        return total_score

    def deal_to_player(self, deck, hand):
        """Deal a card to a player from the deck. The score is then checked and if the have a score above 21 they
     get a score of 0. We return True if they are still below 21 or False if the score goes above i.e. when it is zero."""
        player_good = False
        hand.append(self.playing_card.deal_a_card(deck))
        if self.score_hand(hand) > 0:
            player_good = True
        return player_good

    def valid_deal_input(self):
        """Get an input of "D"eal or "S"tick from the user, validates only "D" or "S" has been entered and the
     returns the answer in upper case. A while loop is used to prompt the user till the enter a valid response"""
        """Function to get a valid user input for the deal_to_user function"""
        allowed_answers = ["D", "S"]
        answer = input("Please select (D)raw or (S)tick: ")
        while answer.upper() not in allowed_answers:
            answer = input("That is not a valid input. Please select (D)raw or (S)tick: ")
        return answer.upper()

    def deal_to_user(self, deck, hand):
        """The user will be displayed their hand and can either request to be dealt a new ard from the deck or they
     can stick so stop and move on. When you are dealt a card we determine the score, if you go over the limit 21 you loose
     and are bust. In this case we move on."""
        answer = "D"
        while answer == "D":
            print("Your hand is", hand)
            answer = self.valid_deal_input()
            if answer == "D":
                if not self.deal_to_player(deck, hand):
                    answer = "F"
                    print("Sorry you have gone over the score and are bust", hand)

    def find_winner(self, hands):
        """Go through each of the hands and determine the score. If the score is better than the previous score we
     replace the previous score, so we only store the highest score so far. If we have a draw both players are added to
     the to the previous player list. To determine a winner if you have the same score you win if you have five cards."""
        previous_player = []
        previous_hand = []
        previous_score = 0

        for counter in range(0, len(hands)):
            current_score = self.score_hand(hands[counter])
            if previous_score < current_score or (previous_score == current_score and (
                    len(hands[counter]) == self.good_number_of_cards and len(
                    previous_hand) != self.good_number_of_cards)):
                previous_player = [counter]
                previous_hand = hands[counter]
                previous_score = current_score
            elif previous_score == current_score:
                previous_player.append(counter)

        return previous_player

    def initialise_computer_risk(self, number_of_player):
        """The  function determines the risk for each computer player. The risk is determined by getting a random
     number. So if there risk level is nine they will stick if the have a score of twelve or above i.e. 21 minus risk
     level. If they have nine they will request an additional card."""
        computer_risk = {}
        for counter in range(1, number_of_player):
            computer_risk[counter] = random.randint(2, 9)
        return computer_risk

    def deal_to_computer(self, deck, hands, computer_risk):
        """The computer will have a risk, the number on or above they will stick at i.e. not ask for more cards. So
     if there risk level is nine they will stick if the have a score of twelve or above. If they have nine they will request an
     additional card. One gap is the computer does not know if they have an Ace. If the have an ace it could be sensible to
     request another card, this would require a second risk level for when you have an Ace."""
        for counter in computer_risk.keys():
            score = self.score_hand(hands[counter])
            while score > 0 and score + computer_risk[counter] < self.winning_score and len(deck) > 0:
                result = self.deal_to_player(deck, hands[counter])
                score = self.score_hand(hands[counter])

    def black_jack(self, deck, hands, computer_risk):
        """The Black Jack method is passed a deck of playing cards, a starting deal of two cards each and the level
     of risk for the computer. The cards need to add up to 21 or less. If you go above 21 you are bust (loose). First the
     user has the opportunity to request more cards to be dealt, one at a time. The computer will have a risk, the number
     on or above they will stick at i.e. not ask for more cards. Once all the cards have been dealt we determine the winner
     i.e. the closest to 21."""
        self.deal_to_user(deck, hands[self.playing_card.user_hand])
        self.deal_to_computer(deck, hands, computer_risk)
        players = self.find_winner(hands)
        if len(players) == 1:
            print("Player " + str(players[0]) + " is the winner")
        else:
            for player in players:
                print("Player " + str(player) + " draw")
        print(hands)

    def main(self):
        """"Get the number of players, generate the deck of cards and work out the computer players risk."""
        number_of_players = int(input("Please enter the number of players, max is six"))
        deck = self.playing_card.generate_deck()
        deck = self.playing_card.shuffle_cards(deck)
        hands = self.playing_card.deal_cards(deck, 2, number_of_players)
        computer_risk = self.initialise_computer_risk(number_of_players)
        self.black_jack(deck, hands, computer_risk)


# This allows the main to be called only when you run this file.
if __name__ == "__main__":
    blackjack = BlackJack()
    blackjack.main()
