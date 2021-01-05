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
    SOLVEDBOARD = getStartingBoard()
    allMoves = []
    while True:
        slideTo = None
        msg = 'Click tile or press arrow keys to slide.' 
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
def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()

def getStartingBoard():

            counter = 1
            board = []
            for x in range(Board_Width):
                column = []
                for y in range(Board_Height):
                    column.append(counter)
                    counter += Board_Width
                board.append(column)
                counter -= Board_Width * (Board_Height - 1) + Board_Width - 1

            board[Board_Width - 1][Board_Height - 1] = BLANK
            return board

def getBlankPosition(board):
    # Return the x and y of board coordinates of the blank space.
    for x in range(Board_Width):
        for y in range(Board_Height):
            if board[x][y] == BLANK:
                return (x, y)

            def makeMove(board, move):
                
                blankx, blanky = getBlankPosition(board)

                if move == Up:
                    board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
                elif move == Down:
                    board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
                elif move == Left:
                    board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
                elif move == Right:
                    board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]
def isValidMove(board, move):
    blankx, blanky = getBlankPosition(board)
    return (move == Up and blanky != len(board[0]) - 1) or \
           (move == Down and blanky != 0) or \
           (move == Left and blankx != len(board) - 1) or \
           (move == Right and blankx != 0)

def getRandomMove(board, lastMove=None):
    # start with a full list of all four moves
    validMoves = [Up, Down, Left, Right]

    # remove moves from the list as they are disqualified
    if lastMove == Up or not isValidMove(board, Down):
        validMoves.remove(Down)
    if lastMove == Down or not isValidMove(board, Up):
        validMoves.remove(Up)
    if lastMove == Left or not isValidMove(board, Right):
        validMoves.remove(Right)
    if lastMove == Right or not isValidMove(board, Left):
        validMoves.remove(Left)

    # return a random move from the list of remaining moves
    return random.choice(validMoves)


def getLeftTopOfTile(tileX, tileY):
    left = X + (tileX * Square_Size) + (tileX - 1)
    top = Y + (tileY * Square_Size) + (tileY - 1)
    return (left, top)

def getSpotClicked(board, x, y):
    # from the x & y pixel coordinates, get the x & y board coordinates
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY)
            tileRect = pygame.Rect(left, top, Square_Size, Square_Size)
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)

def drawTile(tilex, tiley, number, adjx=0, adjy=0):
    # draw a tile at board coordinates tilex and tiley, optionally a few
    # pixels over (determined by adjx and adjy)
    left, top = getLeftTopOfTile(tilex, tiley)
    pygame.draw.rect(Display_SURF, Square_Color, (left + adjx, top + adjy, Square_Size, Square_Size))
    textSurf = Font.render(str(number), True, Text_Color)
    textRect = textSurf.get_rect()
    textRect.center = left + int(Square_Size / 2) + adjx, top + int(Square_Size / 2) + adjy
    Display_SURF.blit(textSurf, textRect)

    
def makeText(text, color, bgcolor, top, left):
    # create the Surface and Rect objects for some text.
    textSurf = Font.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)