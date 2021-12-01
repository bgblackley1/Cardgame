import unittest
from src.BlackJack import BlackJack


class SnapTest(unittest.TestCase):
    hand = BlackJack()

    def test_score_hand(self):
        self.score = self.hand.score_hand(['CK', 'D8'])
        self.assertEqual(18, self.score)

    def test_deal_to_player(self):
        self.assertEqual(True, self.hand.deal_to_player(['C2'], ['C8', 'DK']))




def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
