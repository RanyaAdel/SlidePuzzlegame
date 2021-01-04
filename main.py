import pygame, sys, random
from pygame.locals import *
Window_Width = 1000  # width of the main window of the game
Window_Height = 600  # height of the main window of the game
Board_Width = 5  # number of squares in each column
Board_Height = 5  # number of squares in each rows
Square_Size = 100  # size of each square in the game
Speed = 2000  # speed of moving squares
BLANK = None  # the empty square
###############################################
EFFFFF = (239, 255, 255)
White = (255,255,255)
Teal = (0,102,102)
Blue = (0,153,153)
Black = (0, 0, 0)
##############################################
Background_Color = EFFFFF
Square_Color = Blue
Text_Color = White
Border_Color = Teal
Font_Size = 20
Title_Color = Black
Button_Color= EFFFFF
##############################################
X = int((Window_Width - (Square_Size * Board_Width + (Board_Width - 1))) / 2)  # to put the window in the center
Y = int((Window_Height - (Square_Size * Board_Height + (Board_Height - 1))) / 2)  # to put the window in the center
##############################################
Up = 'up'
Down = 'down'
Left = 'left'
Right = 'right'
