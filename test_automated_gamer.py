import unittest
from automated_gamer import win_combinations, idx_board, moves_aligned, automated_player

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


class TestAutomatedPlayer(unittest.TestCase):
    def test_2S_1P_col(self):
        board_test = [[1, 2, 3],
                      ["S", 5, 6],
                      ["S", 8, "P"]]
        self.assertEqual([0, 0], automated_player(board_test, idx_board))

    def test_2S_1P_diag(self):
        board_test = [["P", 2, "S"],
                      ["S", 5, 6],
                      ["S", 8, "P"]]
        self.assertEqual([1, 1], automated_player(board_test, idx_board))

    def test_2S_1P_row(self):
        board_test = [["P", 2, 3],
                      ["S", 5, "P"],
                      ["S", 8, "S"]]
        self.assertEqual([2, 1], automated_player(board_test, idx_board))

    def test_2P_1S_col(self):
        board_test = [[1, 2, "P"],
                      [4, 5, 6],
                      ["S", "S", "P"]]
        self.assertEqual([1, 2], automated_player(board_test, idx_board))

    def test_2P_1S_row(self):
        board_test = [["P", 2, "P"],
                      [4, 5, "S"],
                      ["S", "S", "P"]]
        self.assertEqual([0, 1], automated_player(board_test, idx_board))

    def test_2P_1S_diag(self):
        board_test = [["P", "S", "P"],
                      [4, 5, "S"],
                      ["S", "P", "P"]]
        self.assertEqual([1, 1], automated_player(board_test, idx_board))

    def test_empty_board_generates_random_coordinates(self):
        board_test = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
        self.assertEqual((2, list),
                         (len(automated_player(board_test, idx_board)),  # checks that we have 2 items in list
                          type(automated_player(board_test, idx_board))))  # checks the return is a list

    def test_1S_0P_generates_random_coordinates(self):
        board_test = [[1, 2, 3],
                      [4, "S", 6],
                      [7, 8, 9]]
        p_coordinates = automated_player(board_test, idx_board)
        self.assertEqual((2, list, False),
                         (len(p_coordinates),  # checks that we have 2 items in list
                          type(p_coordinates),  # checks the return is a list
                          [1, 1] == p_coordinates))  # to ensure is not "S" coordinates [1,1]

    def test_1S_0P_generates_random_coordinates_test2(self):
        board_test = [[1, "P", 3],
                      [4, "S", 6],
                      [7, "S", 9]]
        p_coordinates = automated_player(board_test, idx_board)
        self.assertEqual((2, list, False, False),
                         (len(p_coordinates),  # checks that we have 2 items in list
                          type(p_coordinates),  # checks the return is a list
                          [1, 1] == p_coordinates,  # to ensure is not "S" coordinates [1,1]
                          [2, 1] == p_coordinates))  # to ensure is not "S" coordinates [1,1]

    def test_1P_0S_Pmoves_to_2_or_8(self):
        board_test = [["S", 2, "P"],
                      ["P", "P", "S"],
                      ["S", 8, 9]]
        p_coordinates = automated_player(board_test, idx_board)
        possibilities = [[0, 1], [1, 2]]
        self.assertEqual(True, any(p_coordinates for x in possibilities))  # check if the coordinates are in possibilites


if __name__ == '__main__':
    unittest.main()
