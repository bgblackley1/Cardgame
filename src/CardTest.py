import unittest
from src.PlayingCard import PlayingCard


class CardTest(unittest.TestCase):
    deck = PlayingCard()

    def test_deck_length(self):
        self.assertEqual(52, len(self.deck.generate_deck()))

    def test_shuffle_length(self):
        self.notshuffled = self.deck.generate_deck()
        self.shuffled = self.deck.shuffle_cards(self.notshuffled)
        self.notshuffled = self.deck.generate_deck()
        self.assertNotEqual(self.shuffled, self.notshuffled)

    def test_deal_card(self):
        self.cards = self.deck.generate_deck()
        self.card = self.deck.deal_a_card(self.cards)
        self.assertTrue(self.card not in self.cards)

    def test_trentine_small(self):
        self.cards = self.deck.generate_deck()
        self.deck.trentine_small(self.cards)
        self.assertFalse('C8' in self.cards)

    def test_deal_cards(self):
        self.cards = self.deck.generate_deck()
        self.deck.deal_cards(self.cards, 2, 3)
        self.assertEqual(46, len(self.cards))

    def test_play_a_card(self):
        self.hand = ['C8', 'C9', 'CA']
        self.deck.play_a_card(self.hand, 'C8')
        self.assertFalse('C8' in self.hand)

    def test_is_playing_a_card(self):
        self.hand = ['C8', 'C9', 'CA']
        self.played = self.deck.is_playing_a_card(self.hand, 'C8')
        self.assertEqual(True, self.played)

    def test_convert_face_to_number(self):
        self.card = self.deck.convert_face_to_number('CK')
        self.assertNotEqual('CK', self.card)

    def test_convert_faces_to_numbers(self):
        self.cards = self.deck.generate_deck()
        self.deck.convert_faces_to_numbers(self.cards)
        self.assertFalse('CK' in self.cards)

    def test_convert_number_to_face(self):
        self.card = self.deck.convert_face_to_number('CK')
        self.revert = self.deck.convert_number_to_face(self.card)
        self.assertEqual('CK', self.revert)

    def test_convert_numbers_to_faces(self):
        self.cards = self.deck.generate_deck()
        self.deck.convert_faces_to_numbers(self.cards)
        self.deck.convert_numbers_to_faces(self.cards)
        self.assertTrue('CK' in self.cards)

    def test_sort_hand(self):
        self.hand = ['C9', 'C8', 'CK']
        self.deck.sort_hand(self.hand)
        self.assertNotEqual(['C9', 'C8', 'CK'], self.hand)

    def test_sort_hands(self):
        self.hands = [['C9', 'C8', 'CK'], ['D3', 'DA', 'D9']]
        self.deck.sort_hands(self.hands)
        self.assertNotEqual(['C9', 'C8', 'CK'], ['D3', 'DA', 'D9'], self.hands)


def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
