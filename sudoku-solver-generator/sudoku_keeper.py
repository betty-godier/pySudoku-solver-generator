import pygame

# Display an error message for bad entered value
def raise_error(font2, screen):
    error_text = "WRONG !!! This is not a correct value"
    text1 = font2.render(error_text, 1, (255, 0, 0))
    screen.blit(text1, (20, 520))
    pygame.display.update()
    pygame.time.delay(1000)


# Check if the entered value is correct
def valid(m, i, j, entered_value):
    for it in range(9):
        if m[i][it]== entered_value or m[it][j]== entered_value:
            return False
    it = (i//3) * 3
    jt = (j//3) * 3
    for x in range(it, it + 3):
        for y in range (jt, jt + 3):
            if m[x][y]== entered_value:
                return False
    return True