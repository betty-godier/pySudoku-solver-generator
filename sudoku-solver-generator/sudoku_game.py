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
    val = 0

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

    # game specific fonts
    font1 = pygame.font.SysFont("comicsans", 30)
    font2 = pygame.font.SysFont("comicsans", 15)

    return screen, dif, default_grid, font1, font2