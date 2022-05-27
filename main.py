import pygame as pg
from engine import Engine
import time
# Constants
SCREEN_WIDTH = SCREEN_HEIGHT = 512
SQUARE_SIZE = SCREEN_WIDTH//8
FPS = 15  # used for animation
IMAGES = {}

eng = Engine()


# Load Images once and store them for later use
def load_images():
    pieces = ["bp", "bR", "bN", "bB", "bQ", "bK", "wp", "wR", "wN", "wB", "wQ", "wK"]

    for piece in pieces:
        IMAGES[piece] = pg.image.load("images/" + piece + ".png")


#read current board state
def piece_color(col, row):
    if eng.board[col][row].startswith('w'):
        #eng.whoz_move = "white"
        return "white"
    elif eng.board[col][row].startswith('b'):
        #eng.whoz_move = "black"
        return "black"


def toggle_player():
    if eng.whoz_move == "white":
        eng.whoz_move = "black"
    elif eng.whoz_move == "black":
        eng.whoz_move = "white"


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

                #current piece color pressed == same color turn, then move
                if click_count % 2 == 1:
                    piece_col = piece_color(col, row)
                print("Piece color:", piece_col)
                print("Engine whoz move:", eng.whoz_move)

                if click_count % 2 == 0 and piece_col == eng.whoz_move:
                    # make move only if its correct players turn
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
    for r in range(8):
        for c in range(8):
            piece = eng.board[r][c]  # get current state board and draws it
            if piece != "##":
                screen.blit(IMAGES[piece], pg.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


#move is a tuple eg (1, 0) (2, 0)
def make_move(screen, move):
    start = move[0]
    to = move[1]
    # find the piece placed at start coordinate and blit it to "to" coordinate

    # remove the image from starting coordinate and move it to destination coordinate
    screen.blit(IMAGES[eng.board[start[0]][start[1]]], (to[1] * SQUARE_SIZE, to[0] * SQUARE_SIZE))

    board_color = [pg.Color("white"), pg.Color("brown")]
    color = board_color[(start[0] + start[1]) % 2]
    pg.draw.rect(screen, color, (start[1] * SQUARE_SIZE, start[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pg.display.update()

    #update the board list after move is made
    eng.board[to[0]][to[1]] = eng.board[start[0]][start[1]]
    eng.board[start[0]][start[1]] = "##"

    # after playing a move, toggle the player
    toggle_player()

if __name__ == '__main__':
    main()

