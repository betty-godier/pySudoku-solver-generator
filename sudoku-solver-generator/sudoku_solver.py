import pygame
from sudoku_keeper import valid 
from sudoku_draw import draw, draw_box

def solve(grid, i, j, screen, dif, font1):
    while grid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if valid(grid, i, j, it)== True:
            grid[i][j]= it
            global x, y
            x = i
            y = j
            screen.fill((255, 255, 255))
            draw(grid, pygame, screen, dif, font1)
            draw_box(screen, pygame, x, y, dif)
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j, screen, dif, font1)== 1:
                return True
            else:
                grid[i][j]= 0
                screen.fill((255, 255, 255))
                draw(grid, pygame, screen, dif, font1)
                draw_box(screen, pygame, x, y, dif)
                pygame.display.update()
                pygame.time.delay(50)
        return False