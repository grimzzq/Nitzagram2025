import pygame

import constants
from constants import *
from helpers import screen


class Post:
    def __init__(self, image=None, description="", location="", likes=0, comments=None):
        self.image = image 
        self.description = description
        self.location = location
        self.likes = likes
        self.comments = comments if comments is not None else []
        self.comments_display_index = 0 

    def display(self):
        if self.image:
            screen.blit(self.image, (constants.POST_X_POS, constants.POST_Y_POS))


        font = pygame.font.SysFont('chalkduster.ttf',TEXT_POST_FONT_SIZE)
        description_surface = font.render(self.description, True, WHITE)
        screen.blit(description_surface, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

        location_surface = font.render(f"📍 {self.location}", True, LIGHT_GRAY)
        screen.blit(location_surface, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        # Display Likes
        likes_surface = font.render(f"❤️ {self.likes} Likes", True, WHITE)
        screen.blit(likes_surface, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

        # Display Comments
        self.display_comments()

    def display_comments(self):
        position_index = self.comments_display_index
        comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)

        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            view_more_button = comment_font.render("View more comments...", True, LIGHT_GRAY)
            screen.blit(view_more_button, (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))

        for i in range(NUM_OF_COMMENTS_TO_DISPLAY):
            if position_index >= len(self.comments):
                position_index = 0  
            self.comments[position_index].display(i) 
            position_index += 1

