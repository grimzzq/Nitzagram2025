import pygame
import post
from helpers import screen
from constants import *
class Text_Post(post):
    def __init__(self, username, location, description, likes_counter, comments,text,textt):
        super().__init__(username,location,description,likes_counter,comments)
        font = pygame.font.Font('freesanbold.ttf',TEXT_POST_FONT_SIZE)
        self.textt = font.render(text,True,BLACK)

    def display(self):
        screen.blit(self.textt, [POST_X_POS,POST_Y_POS])
        super().display()

