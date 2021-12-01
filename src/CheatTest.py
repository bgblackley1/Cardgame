import unittest
from src.Cheat import Cheat

class CheatTest(unittest.TestCase):
    deck = Cheat()

    def test_deal_deck(self):
        deck = self.deck.deal_deck(4)
        self.assertEqual(52/4, len(deck[0]))

    def test_print_cards(self):
        player = 0
        self.assertEqual([1,2,3], self.deck.print_cards([[1,2,3],[],[]], player))

    def test_validate_entry(self):
        self.assertEqual(True, self.deck.validate_entry([['C6', 'D6']], 0, ['C6', 'D6']))

    def test_remove_cards(self):
        self.assertEqual([['C6']], self.deck.remove_cards([['C6', 'D6', 'H6']], 0, ['D6', 'H6']))



def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()


