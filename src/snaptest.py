import unittest
from src.Snap import Snap


class SnapTest(unittest.TestCase):
    snap = Snap()

    def test_initialise_score(self):
        self.init = self.snap.initialise_score()
        self.assertEqual(self.init,[{"turn": True, "score": 0}, {"turn": False, "score": 0}])

    def test_is_snap(self):
        self.assertEqual(True, self.snap.is_snap('C8', 'CK'))

    def test_play_card(self):
        self.hands = [['C8', 'H4'], ['DK', 'S2']]
        self.card = self.snap.play_card(0, self.hands, 2)
        self.assertFalse(self.card in self.hands[0] and self.card in self.hands[1])


def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
