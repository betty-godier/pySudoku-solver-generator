import pygame
from sudoku_game import initialize_game
from sudoku_rules import rules
from sudoku_draw import draw_box, draw

# get the grid coordinates (x, y) based on the mouse position pos (x, y) when the user clicks on the window.
x = 0
y = 0
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif
    return x, y

# main game loop
running = True
screen, dif, default_grid, font1, font2 = initialize_game()

while running:
    screen.fill((255, 255, 255))  # Fill the screen with white color
    # loop through register events in event.get()
    for event in pygame.event.get():
        # quit the game
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position when clicked
            mouse_pos = pygame.mouse.get_pos()
            get_cord(mouse_pos)  # Update the grid coordinates based on the click position
    draw(default_grid, pygame, screen, dif, font1)  # Draw the Sudoku grid
    draw_box(screen, pygame, x, y, dif)  # Draw the highlight box for the selected cell
    rules(font2, screen) # Display game instructions

    pygame.display.update()  # Update the display

pygame.quit()  # Quit the game when the loop exits