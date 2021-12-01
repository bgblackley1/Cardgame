from operator import add
from PlayingCard import PlayingCard

deck = PlayingCard()


class hand():
    def __init__(self):
        self.__deck = deck.generate_deck()
        self.__shuffleddeck = deck.shuffle_cards(self.__deck)
        deck.convert_faces_to_numbers(self.__shuffleddeck)
        self.__dealcards()
        self.__check_hands()
        self.__combine_hands()
        self.__hand_score()
        self.__check_winner()

    def __dealcards(self):
        players = int(input('How many players: '))
        self.__hands = deck.deal_cards(self.__shuffleddeck, 2, players)
        self.__centre_cards = deck.deal_cards(self.__shuffleddeck, 5, 1)[0]

    def __check_hands(self):
        self.__scorecard = []
        for hand in self.__hands:
            self.__scorecard.append(self.__check_hand(hand))
        self.__scorecard.append(self.__check_hand(self.__centre_cards))

    def __check_hand(self, hand):
        suits = [0] * 4
        number = [0] * 14
        for card in hand:
            number[int(card[1:])] += 1
            if card[0] == 'H':
                suits[0] += 1
            if card[0] == 'D':
                suits[1] += 1
            if card[0] == 'S':
                suits[2] += 1
            if card[0] == 'C':
                suits[3] += 1
        return ([number, suits])

    def __combine_hands(self):
        for i in range(0, len(self.__scorecard) - 1):
            self.__scorecard[i][0] = list(map(add, self.__scorecard[i][0], self.__scorecard[-1][0]))
            self.__scorecard[i][1] = list(map(add, self.__scorecard[i][1], self.__scorecard[-1][1]))
        self.__scorecard.pop(-1)

    def __hand_score(self):
        self.__scores = []
        for hand in self.__scorecard:
            score = 0
            if 2 in hand[0]:
                score = 1
            if hand[0].count(2) == 2:
                score = 2
            if 3 in hand[0]:
                score = 3
            straight = 0
            for i in range(1, len(hand[0]) - 1):
                if hand[0][i] != 0 and ((hand[0][i - 1] != 0) or hand[0][i + 1] != 0):
                    straight += 1
                elif straight != 5:
                    straight = 0
            if straight == 5:
                score = 4
            if 5 in hand[1]:
                score = 5
            if 2 in hand[0] and 3 in hand[0]:
                score = 6
            if 4 in hand[0]:
                score = 7
            if straight == 5 and 5 in hand[1]:
                straight_flush = self.__check_straight_flush(hand)
                if straight_flush == True:
                    score = 8
            if straight == 5 and 5 in hand[1] and hand[0][-1] != -1:
                score = 9
            self.__scores.append(score)

    def __check_straight_flush(self, hand):
        deck.convertNumbersToFaces(hand[0])
        joint_hand = hand[0] + self.__centre_cards
        joint_hand.sort()
        joint_hand.append()
        straight_flush = False
        suit = 0
        for i in range(1, len(joint_hand) - 1):
            if joint_hand[i][0] == joint_hand[i + 1][0] and int(joint_hand[i][:1]) == int(joint_hand[i][:1]) - 1:
                suit += 1
            if suit == 4:
                straight_flush = True
            else:
                suit = 0
        return (straight_flush)

    def __check_winner(self):
        if self.__scores.count(max(self.__scores)) == 1:
            highest = 0
            position = 0
            draw = False
            for i in range(0, len(self.__scores)):
                if self.__scores[i] > highest:
                    highest = self.__scores[i]
                    position = i
        else:
            position, highest, draw = self.__multiple_of_the_same()
        hand = self.__hands[position] + self.__centre_cards
        deck.convert_numbers_to_faces(hand)
        if draw == False:
            if highest == 0:
                print('Player ' + str(position + 1) + ' wins with high card')
                print(' '.join(hand))
            if highest == 1:
                print('Player ' + str(position + 1) + ' wins with a pair')
                print(' '.join(hand))
            if highest == 2:
                print('Player ' + str(position + 1) + ' wins with two pairs')
                print(' '.join(hand))
            if highest == 3:
                print('Player ' + str(position + 1) + ' wins with three of a kind')
                print(' '.join(hand))
            if highest == 4:
                print('Player ' + str(position + 1) + ' wins with a straight')
                print(' '.join(hand))
            if highest == 5:
                print('Player ' + str(position + 1) + ' wins with a flush')
                print(' '.join(hand))
            if highest == 6:
                print('Player ' + str(position + 1) + ' wins with a full house')
                print(' '.join(hand))
            if highest == 7:
                print('Player ' + str(position + 1) + ' wins with four of a kind')
                print(' '.join(hand))
            if highest == 8:
                print('Player ' + str(position + 1) + ' wins with a straight flush')
                print(' '.join(hand))
            if highest == 9:
                print('Player ' + str(position + 1) + ' wins with a royal flush')
                print(' '.join(hand))
        else:
            print('Draw')

    def __multiple_of_the_same(self):
        highest = max(self.__scores)
        drawing = []
        for i in range(0, len(self.__scores)):
            if self.__scores[i] == highest:
                drawing.append(i)
        highest_pair = 0
        highest_three = 0
        highest_four = 0
        highest_card = 0
        highest_hand = 0
        draw = False
        for hand in drawing:
            if highest == 0:
                for i in range(0, len(self.__scorecard[hand][0])):
                    if self.__scorecard[hand][0][i] == 1 and i > highest_card:
                        highest_hand = hand
                        highest_card = i
                        draw = False
                    if i == highest_card:
                        draw = True
            if highest == 1 or highest == 2:
                for i in range(0, len(self.__scorecard[hand][0])):
                    if self.__scorecard[hand][0][i] == 2 and i > highest_pair:
                        highest_hand = hand
                        highest_pair = i
                        draw = False
                    if i == highest_card:
                        draw = True
            if highest == 3 or highest == 6:
                for i in range(0, len(self.__scorecard[hand][0])):
                    if self.__scorecard[hand][0][i] == 3 and i > highest_three:
                        highest_hand = hand
                        highest_three = i
                        draw = False
                    if i == highest_card:
                        draw = True
            if highest == 4 or highest == 8:
                straight = 0
                for i in range(1, len(self.__scorecard[hand][0]) - 1):
                    if self.__scorecard[hand][0][i] == self.__scorecard[hand][0][i] - 1:
                        straight += 1
                        if straight == 4 and i > highest_card:
                            highest_hand = hand
                            highest_card = i
                            draw = False
                    else:
                        straight = 0
                    if i == highest_card:
                        draw = True
            if highest == 5:
                flush_suit = max(self.__scorecard[hand][1])
                suits = ['H', 'D', 'S', 'C']
                jointhand = self.__hands[hand] + self.__centre_cards
                for i in range(0, len(jointhand)):
                    if jointhand[i][0] == suits[flush_suit] and jointhand[i][:1] > highest_card:
                        highest_hand = hand
                        highest_card = jointhand[i][:1]
                        draw = False
                    if jointhand[i][:1] == highest_card:
                        draw = True
            if highest == 7:
                for i in range(0, len(self.__scorecard[hand][0])):
                    if self.__scorecard[hand][0][i] == 4 and i > highest_card:
                        highest_hand = hand
                        highest_four = i
                        draw = False
                    if i == highest_card:
                        draw = True
        return (highest_hand, highest, draw)


if __name__ == '__main__':
    hand()
