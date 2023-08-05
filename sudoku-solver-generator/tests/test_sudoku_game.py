import unittest
from sudoku_game import initialize_game, result

class TestSudokuGame(unittest.TestCase):

    def test_initialize_game(self):
        # Test the initialize_game function
        screen, dif, entered_value, default_grid, reinit_grid, empty_grid, key_value_map, font1, font2 = initialize_game()
        self.assertIsNotNone(screen)
        self.assertIsNotNone(dif)
        self.assertEqual(entered_value, 0)
        self.assertIsInstance(default_grid, list)
        self.assertIsInstance(reinit_grid, list)
        self.assertIsInstance(empty_grid, list)
        self.assertIsInstance(key_value_map, dict)
        self.assertIsNotNone(font1)
        self.assertIsNotNone(font2)

    def test_result(self):
        # Test the result function
        # Create a surface to draw on
        surface = pygame.Surface((500, 500))

        # Call the result function
        result(font1, surface)

        # Assert that the result message is drawn correctly on the surface
        self.assertTrue((0, 0, 0) in surface.get_at((20, 570)))

if __name__ == '__main__':
    unittest.main()
