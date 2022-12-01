import unittest
from utils import convert_pos_to_idx, check_winner


class TestConvertPositionToIndex(unittest.TestCase):
    # REMINDER: position (x, y) = Index (col, row) however the return of the func is (row, col)
    # Starting point for positions is always top left corner of the board
    def test_100_100_as_0_0(self):
        self.assertEqual((0, 0), convert_pos_to_idx((100, 100)))

    def test_300_300_as_1_1(self):
        self.assertEqual((1, 1), convert_pos_to_idx((300, 300)))

    def test_500_500_as_2_2(self):
        self.assertEqual((2, 2), convert_pos_to_idx((500, 500)))

    def test_199_399_as_1_0(self):
        self.assertEqual((1, 0), convert_pos_to_idx((199, 399)))

    def test_599_399_as_1_2(self):
        self.assertEqual((1, 2), convert_pos_to_idx((599, 399)))

    def test_000_599_as_2_0(self):
        self.assertEqual((2, 0), convert_pos_to_idx((000, 599)))

    def test_200_400_as_2_1(self):
        self.assertEqual((2, 1), convert_pos_to_idx((200, 400)))


class TestCheckWinner(unittest.TestCase):
    def test_P_row_win(self):
        board = [["P", "P", "P"],
                 ["S", 5, 6],
                 ["S", 8, 9]]
        self.assertEqual("P", check_winner(board))

    def test_S_col_win(self):
        board = [["S", "P", "P"],
                 ["S", 5, 6],
                 ["S", 8, 9]]
        self.assertEqual("S", check_winner(board))

    def test_game_unfinished_none_wins(self):
        board = [[1, "P", "P"],
                 ["S", 5, 6],
                 ["S", 8, 9]]
        self.assertEqual(None, check_winner(board))

    def test_draw_none_wins(self):
        board = [["S", "P", "P"],
                 ["P", "S", "S"],
                 ["S", "S", "P"]]
        self.assertEqual(None, check_winner(board))

    def test_zero_movements_none_wins(self):
        board = [[1, 2, 3],
                 [4, 5, 6],
                 [5, 8, 9]]
        self.assertEqual(None, check_winner(board))

if __name__ == '__main__':
    unittest.main()
