import unittest
from automated_gamer import win_combinations, idx_board, moves_aligned

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


class TestWinCombinations(unittest.TestCase):
    def test_empty_board(self):
        result = {1: [[1, 2, 3], [[0, 0], [0, 1], [0, 2]]],
                  2: [[4, 5, 6], [[1, 0], [1, 1], [1, 2]]],
                  3: [[7, 8, 9], [[2, 0], [2, 1], [2, 2]]],
                  4: [[1, 4, 7], [[0, 0], [1, 0], [2, 0]]],
                  5: [[2, 5, 8], [[0, 1], [1, 1], [2, 1]]],
                  6: [[3, 6, 9], [[0, 2], [1, 2], [2, 2]]],
                  7: [[1, 5, 9], [[0, 0], [1, 1], [2, 2]]],
                  8: [[3, 5, 7], [[0, 2], [1, 1], [2, 0]]]}
        self.assertEqual(result, win_combinations(board, idx_board))


class TestMovesAligned(unittest.TestCase):
    def test_empty_board_none(self):
        self.assertEqual(False, moves_aligned("S", 2, board, idx_board))

    def test_1S_2empty_row(self):
        board_test = [[1, 2, 3],
                      ["S", 5, 6],
                      [7, 8, "P"]]
        self.assertEqual((["S", 5, 6], [[1, 0], [1, 1], [1, 2]]), moves_aligned("S", 1, board_test, idx_board))

    def test_2S_1empty_row(self):
        board_test = [[1, 2, 3],
                      ["S", "S", 6],
                      [7, 8, "P"]]
        self.assertEqual((["S", "S", 6], [[1, 0], [1, 1], [1, 2]]), moves_aligned("S", 2, board_test, idx_board))

    def test_2S_0empty_row(self):
        board_test = [[1, 2, 3],
                      ["S", "S", "P"],
                      [7, 8, "P"]]
        self.assertEqual(False, moves_aligned("S", 2, board_test, idx_board))

    def test_1S_2empty_col(self):
        # should ignore row 2 where ["S", 5, "P"] because S cannot make a line there anymore
        board_test = [[1, 2, 3],
                      ["S", 5, "P"],
                      [7, 8, "P"]]
        self.assertEqual(([1, "S", 7], [[0, 0], [1, 0], [2, 0]]), moves_aligned("S", 1, board_test, idx_board))

    def test_1S_2empty_diagonal(self):
        # should ignore row 2 where ["S", 5, "P"] because S cannot make a line there anymore
        # should ignore col 2 where ["P", "S", 7] because S cannot make a line there anymore
        board_test = [["P", 2, "S"],
                      ["S", 5, "P"],
                      [7, 8, "P"]]
        self.assertEqual((["S", 5, 7], [[0, 2], [1, 1], [2, 0]]), moves_aligned("S", 1, board_test, idx_board))

    def test_2S_1empty_diagonal(self):
        # should ignore row 2 where ["S", "S", "P"] because S cannot make a line there anymore
        board_test = [["P", 2, "S"],
                      ["S", "S", "P"],
                      [7, 8, "P"]]
        self.assertEqual((["S", "S", 7], [[0, 2], [1, 1], [2, 0]]), moves_aligned("S", 2, board_test, idx_board))

    def test_2S_1empty_one_movement_left(self):
        board_test = [["P", 2, "S"],
                      ["S", "S", "P"],
                      ["P", "S", "P"]]
        self.assertEqual(([2, "S", "S"], [[0, 1], [1, 1], [2, 1]]), moves_aligned("S", 2, board_test, idx_board))

    def test_no_movements_left(self):
        board_test = [["P", "P", "S"],
                      ["S", "S", "P"],
                      ["P", "S", "P"]]
        self.assertEqual(False, moves_aligned("S", 2, board_test, idx_board))





if __name__ == '__main__':
    unittest.main()
