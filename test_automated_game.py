import unittest
from automated_gamer import win_combinations, idx_board

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


if __name__ == '__main__':
    unittest.main()
