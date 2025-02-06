import pygame
import post
from helpers import screen
from constants import *
class ImagePost(post):
    def __init__(self, username, location, description, likes_counter, comments,image):
        super().__init__(username,location,description,likes_counter,comments)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))



    def display(self):
        screen.blit(self.image,[POST_X_POS,POST_Y_POS])

        super().display()

