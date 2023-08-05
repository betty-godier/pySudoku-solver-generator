import pygame
from sudoku_game import initialize_game, result
from sudoku_rules import rules
from sudoku_draw import draw_box, draw, draw_val
from sudoku_solver import solve
from sudoku_keeper import valid, raise_error

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
is_cell_selected = 0
is_result_shown = 0
is_reset = 0
has_error = 0

screen, dif, entered_value, default_grid, empty_grid, key_value_map, font1, font2 = initialize_game()

while running:
    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # loop through register events in event.get()
    for event in pygame.event.get():
        # quit the game
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position when clicked
            is_cell_selected = 1
            mouse_pos = pygame.mouse.get_pos()
            get_cord(mouse_pos)  # Update the grid coordinates based on the click position
            # get the entered_value
        if event.type == pygame.KEYDOWN:
            # check if the pressed key is in the key_value_map
            if event.key in key_value_map:
                entered_value = key_value_map[event.key]
            if event.key == pygame.K_LEFT:
                x-= 1
                is_cell_selected = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                is_cell_selected = 1
            if event.key == pygame.K_UP:
                y-= 1
                is_cell_selected = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                is_cell_selected = 1
            if event.key == pygame.K_RETURN:
                is_result_shown = 1
            if event.key == pygame.K_r:
                is_reset = 0
                has_error = 0
                is_result_shown = 0
                sudoku_grid = [row[:] for row in empty_grid]

            if event.key == pygame.K_d:
                is_reset = 0
                has_error = 0
                is_result_shown = 0
                sudoku_grid =[
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
    if is_result_shown == 1:
        if solve(default_grid, 0, 0, screen, dif, font1)== False:
            has_error = 1
        else:
            is_reset = 1
        is_result_shown = 0

    # Fill the cell with the entered value (if any)
    if entered_value != 0:
        draw_val(entered_value, font1, screen, x, y, dif) # Fill the cell with the entered value 
        if valid(default_grid, int(x), int(y), entered_value)== True:
            default_grid[int(x)][int(y)]= entered_value
            is_cell_selected = 0
        else:
            default_grid[int(x)][int(y)]= 0
            raise_error(font1, screen)
        entered_value = 0
    if has_error == 1:
        raise_error(font2, screen)
    if is_reset == 1:
        result(font1, screen)
    draw(default_grid, pygame, screen, dif, font1)  # Draw the Sudoku grid
    if is_cell_selected == 1:
        draw_box(screen, pygame, x, y, dif)  # Draw the highlight box for the selected cell
    rules(font2, screen) # Display game instructions

    pygame.display.update()  # Update the display

pygame.quit()  # Quit the game when the loop exits