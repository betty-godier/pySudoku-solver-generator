import unittest
import pygame
from sudoku_draw import draw_box, draw, draw_val

class TestSudokuDraw(unittest.TestCase):

    def setUp(self):
        # Initialize Pygame for testing (not necessary for actual drawing)
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.dif = 500 / 9
        self.font = pygame.font.SysFont("comicsans", 30)

    def test_draw_box(self):
        # Test the draw_box function
        # Create a surface to draw on
        surface = pygame.Surface((500, 500))

        # Draw a box at position (1, 1) on the surface
        draw_box(surface, pygame, 1, 1, self.dif)

        # Assert that the box is drawn correctly on the surface
        self.assertTrue((255, 0, 0) in surface.get_at((1 * self.dif, 1 * self.dif)))
        self.assertTrue((255, 0, 0) in surface.get_at(((1 + 1) * self.dif, (1 + 1) * self.dif)))

    def test_draw(self):
        # Test the draw function
        # Create a surface to draw on
        surface = pygame.Surface((500, 500))

        # Create a Sudoku grid with some numbers
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

        # Draw the Sudoku grid on the surface
        draw(grid, pygame, surface, self.dif, self.font)

        # Assert that the numbers are drawn correctly on the surface
        self.assertTrue((0, 0, 0) in surface.get_at((0 * self.dif + 15, 0 * self.dif + 15)))
        self.assertTrue((0, 0, 0) in surface.get_at((1 * self.dif + 15, 0 * self.dif + 15)))
        self.assertTrue((0, 0, 0) in surface.get_at((0 * self.dif + 15, 1 * self.dif + 15)))
        self.assertTrue((0, 0, 0) in surface.get_at((3 * self.dif + 15, 4 * self.dif + 15)))

    def test_draw_val(self):
        # Test the draw_val function
        # Create a surface to draw on
        surface = pygame.Surface((500, 500))

        # Draw a value '5' at position (2, 2) on the surface
        draw_val(5, self.font, surface, 2, 2, self.dif)

        # Assert that the value '5' is drawn correctly on the surface
        self.assertTrue((0, 0, 0) in surface.get_at((2 * self.dif + 15, 2 * self.dif + 15)))

if __name__ == '__main__':
    unittest.main()
