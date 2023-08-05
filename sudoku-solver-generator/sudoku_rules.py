import pygame

# game rules
def rules(font2, screen):
    error_text1 = "PRESS D TO REINIT AND R TO ERASE"
    error_text2 = "ADD NUMBER AND PRESS ENTER TO VIEW THEM"
    text1 = font2.render(error_text1, 1, (0, 0, 0))
    text2 = font2.render(error_text2, 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))