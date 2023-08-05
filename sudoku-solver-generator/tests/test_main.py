import unittest
import pygame
from main import *

class TestSudokuGame(unittest.TestCase):

    def setUp(self):
        # Initialize Pygame for testing
        pygame.init()

    def test_get_cord(self):
        # Test the get_cord function
        pos = (150, 200)
        x, y = get_cord(pos)
        self.assertEqual(x, 16)
        self.assertEqual(y, 22)

    def test_valid_key_value_map(self):
        # Test the key_value_map dictionary
        key_event_1 = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_1)
        key_event_2 = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_2)
        key_event_3 = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_3)
        self.assertEqual(key_value_map[key_event_1.key], 1)
        self.assertEqual(key_value_map[key_event_2.key], 2)
        self.assertEqual(key_value_map[key_event_3.key], 3)

    def test_valid_move(self):
        # Test the movement keys
        key_event_left = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
        key_event_right = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
        key_event_up = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
        key_event_down = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)

        x, y = 0, 0
        get_cord((150, 200))  # Set the coordinates for testing
        self.assertEqual(x, 16)
        self.assertEqual(y, 22)

        # Test moving left
        pygame.event.post(key_event_left)
        main()  # Run the main loop once
        self.assertEqual(x, 15)
        self.assertEqual(y, 22)

        # Test moving right
        pygame.event.post(key_event_right)
        main()
        self.assertEqual(x, 16)
        self.assertEqual(y, 22)

        # Test moving up
        pygame.event.post(key_event_up)
        main()
        self.assertEqual(x, 16)
        self.assertEqual(y, 21)

        # Test moving down
        pygame.event.post(key_event_down)
        main()
        self.assertEqual(x, 16)
        self.assertEqual(y, 22)

if __name__ == '__main__':
    unittest.main()
