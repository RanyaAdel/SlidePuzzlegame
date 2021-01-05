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


def main():
    global Speed_Clock, Display_SURF, Font, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

    pygame.init()
    Speed_Clock = pygame.time.Clock()
    Display_SURF = pygame.display.set_mode((Window_Width, Window_Height))
    pygame.display.set_caption('Slide Puzzle')
    Font = pygame.font.Font('freesansbold.ttf', Font_Size)

    NEW_SURF, NEW_RECT = makeText('New Game', Title_Color, Button_Color, Window_Width - 120, Window_Height - 60)
    SOLVE_SURF, SOLVE_RECT = makeText('Solve', Title_Color, Button_Color, Window_Width - 120, Window_Height - 30)

    mainBoard, solutionSeq = generateNewPuzzle(80)
    SOLVEDBOARD = getStartingBoard()
    allMoves = []
    while True:
        slideTo = None
        msg = 'Click tile .'
        if mainBoard == SOLVEDBOARD:
            msg = 'Solved!'

        drawBoard(mainBoard, msg)
        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                if (spotx, spoty) == (None, None):


                    if NEW_RECT.collidepoint(event.pos):
                        mainBoard, solutionSeq = generateNewPuzzle(80)
                        allMoves = []
                    elif SOLVE_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, solutionSeq + allMoves)
                        allMoves = []
                else:

                    blankx, blanky = getBlankPosition(mainBoard)
                    if spotx == blankx + 1 and spoty == blanky:
                        slideTo = Left
                    elif spotx == blankx - 1 and spoty == blanky:
                        slideTo = Right
                    elif spotx == blankx and spoty == blanky + 1:
                        slideTo = Up
                    elif spotx == blankx and spoty == blanky - 1:
                        slideTo = Down

        if slideTo:
            slideAnimation(mainBoard, slideTo, 'Click tile .', 8)
            makeMove(mainBoard, slideTo)
            allMoves.append(slideTo)
        pygame.display.update()
        Speed_Clock.tick(Speed)