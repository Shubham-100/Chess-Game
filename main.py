import pygame as pg
from engine import Engine
import time
# Constants
SCREEN_WIDTH = SCREEN_HEIGHT = 512
SQUARE_SIZE = SCREEN_WIDTH//8
FPS = 15  # used for animation
IMAGES = {}


# Load Images once and store them for later use
def load_images():
    pieces = ["bp", "bR", "bN", "bB", "bQ", "bK", "wp", "wR", "wN", "wB", "wQ", "wK"]

    for piece in pieces:
        IMAGES[piece] = pg.image.load("images/" + piece + ".png")


def main():
    # Initialize pygame and set up drawing canvas
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Chess Masters")
    clock = pg.time.Clock()
    load_images()

    # Game loop

    running = True
    click_count = 0
    move = []

    clock.tick(FPS)
    draw_board(screen)
    pg.display.flip()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                click_count += 1  # to determine if it's the first click or the second

                if click_count % 2 == 1:  # empty the list since a pair of move has been played
                    move.clear()

                x, y = pg.mouse.get_pos()
                row = x // SQUARE_SIZE
                col = y // SQUARE_SIZE
                move.append((col, row))
                engine = Engine()
                print(move, engine.notation[move[0]])

                if click_count % 2 == 0:
                    make_move(screen, move)




def draw_board(screen):
    # Draw chess board
    board_color = [pg.Color("white"), pg.Color("brown")]

    for r in range(8):
        for c in range(8):
            # If color == 0 then it is light square, else it is dark square
            color = board_color[(r + c) % 2]
            pg.draw.rect(screen, color, (c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Draw pieces
    eng = Engine()
    for r in range(8):
        for c in range(8):
            piece = eng.board[r][c]  # get current state board and draws it
            if piece != "##":
                screen.blit(IMAGES[piece], pg.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def make_move(screen, move):
    start = move[0]
    to = move[1]
    # find the piece placed at start coordinate and blit it to "to" coordinate
    eng = Engine()
    print(eng.board[start[0]][start[1]], "moved")
    screen.blit(IMAGES[eng.board[start[0]][start[1]]], (to[1] * SQUARE_SIZE, to[0] * SQUARE_SIZE))
    pg.display.update()

    #update the board list after move is made

if __name__ == '__main__':
    main()

