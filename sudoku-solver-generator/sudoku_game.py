import pygame

def initialize_game(window_caption="Sudoku", icon_file = 'icon.png'):
    # game font
    pygame.font.init()

    # initialize a 500x600 pixels window
    screen_width = 500
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set the window caption at the beginning of the game
    pygame.display.set_caption(window_caption)

    # set icon
    icon = pygame.image.load(icon_file)
    pygame.display.set_icon(icon)

    dif = 500 / 9
    entered_value = 0

    # default grid
    default_grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0 ,2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    # Define the empty grid with all values set to 0
    empty_grid = [[0 for _ in range(9)] for _ in range(9)]

    # Define a dictionary to map key codes to their corresponding values
    key_value_map = {
        pygame.K_1: 1,
        pygame.K_2: 2,
        pygame.K_3: 3,
        pygame.K_4: 4,
        pygame.K_5: 5,
        pygame.K_6: 6,
        pygame.K_7: 7,
        pygame.K_8: 8,
        pygame.K_9: 9
    }

    # game specific fonts
    font1 = pygame.font.SysFont("comicsans", 20)
    font2 = pygame.font.SysFont("comicsans", 13)

    return screen, dif, entered_value, default_grid, empty_grid, key_value_map, font1, font2

def result(font1, screen):
    result_text = "Game over, Press R or D"
    text1 = font1.render(result_text, 1, (0, 0, 0))
    screen.blit(text1, (20, 570))
