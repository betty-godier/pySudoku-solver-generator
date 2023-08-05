import pygame

# game rules
def rules(font2, screen):
    text1 = font2.render("PRESS D TO REINIT AND R TO ERASE", 1, (0, 0, 0))
    text2 = font2.render("ADD NUMBER AND PRESS ENTER TO VIEW THEM", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))