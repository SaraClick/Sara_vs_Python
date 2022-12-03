import unittest
from automated_gamer import win_combinations

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

class TestWinCombinations(unittest.TestCase):
    def test_empty_board(self):
        result = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.assertEqual(result, win_combinations(board))


if __name__ == '__main__':
    unittest.main()
