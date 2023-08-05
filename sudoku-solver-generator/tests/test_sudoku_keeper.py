import unittest
from sudoku_keeper import valid

class TestSudokuKeeper(unittest.TestCase):

    def test_valid_row(self):
        # Test a valid row in Sudoku grid
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.assertTrue(valid(grid, 0, 0, 5))
        self.assertTrue(valid(grid, 0, 1, 3))
        self.assertTrue(valid(grid, 0, 3, 1))
        self.assertTrue(valid(grid, 4, 3, 8))
        self.assertTrue(valid(grid, 8, 8, 9))

    def test_valid_column(self):
        # Test a valid column in Sudoku grid
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.assertTrue(valid(grid, 0, 0, 5))
        self.assertTrue(valid(grid, 1, 0, 6))
        self.assertTrue(valid(grid, 2, 0, 0))
        self.assertTrue(valid(grid, 2, 1, 9))
        self.assertTrue(valid(grid, 4, 8, 9))

    def test_valid_box(self):
        # Test a valid 3x3 box in Sudoku grid
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.assertTrue(valid(grid, 0, 0, 5))
        self.assertTrue(valid(grid, 0, 1, 3))
        self.assertTrue(valid(grid, 1, 0, 6))
        self.assertTrue(valid(grid, 1, 1, 0))
        self.assertTrue(valid(grid, 2, 2, 8))

if __name__ == '__main__':
    unittest.main()
