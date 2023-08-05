import pygame

# draws a red box around the selected cell to highlight it
def draw_box(screen, pygame, x, y, dif):
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)* dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

# draws the Sudoku grid on the window, including the default values from the grid list
def draw(grid, pygame, screen, dif, font1):
    for i in range(9):
        for j in range (9):
            if grid[i][j]!= 0:
                # fill with teal color when number is in
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
                # fill the grid with default grid number
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
                # calculates the position of the text so that it is centered horizontally and vertically within the cell
                # text1_rect = text1.get_rect(center=(i * dif + dif // 2, j * dif + dif // 2)) 
                # blits the text at the calculated position
                # screen.blit(text1, text1_rect.topleft)
        # draw lines to draw a grid
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

# draws numerical value inside a cell
def draw_val(entered_value, font1, screen, x, y, dif):
    text1 = font1.render(str(entered_value), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))