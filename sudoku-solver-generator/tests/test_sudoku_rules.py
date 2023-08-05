import unittest
import pygame
from sudoku_rules import rules

class TestSudokuRules(unittest.TestCase):

    def setUp(self):
        # Initialize Pygame for testing (not necessary for actual drawing)
        pygame.init()
        self.screen = pygame.Surface((500, 500))
        self.font2 = pygame.font.SysFont("comicsans", 15)

    def test_rules(self):
        # Test the rules function
        # Call the rules function
        rules(self.font2, self.screen)

        # Assert that the rules messages are drawn correctly on the surface
        self.assertTrue((0, 0, 0) in self.screen.get_at((20, 520)))
        self.assertTrue((0, 0, 0) in self.screen.get_at((20, 540)))

if __name__ == '__main__':
    unittest.main()
