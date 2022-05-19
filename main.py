import pygame as pg
from engine import Engine

# Constants
SCREEN_WIDTH = SCREEN_HEIGHT = 512
SQUARE_SIZE = SCREEN_WIDTH//8
FPS = 15  # used for animation
IMAGES = {}


# Load Images once and store them for later use
def load_images(screen):
    pieces = ["bp", "bR", "bN", "bB", "bQ", "bK", "wp", "wR", "wN", "wB", "wQ", "wK"]

    for piece in pieces:
        IMAGES[piece] = pg.image.load("images/" + piece + ".png")


def main():
    # Initialize pygame and set up drawing canvas
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Chess Masters")
    clock = pg.time.Clock()
    load_images(screen)

    # Game loop
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                running = False

        clock.tick(FPS)
        draw_board(screen)
        pg.display.flip()
        pg.display.update()


def draw_board(screen):
    # Draw chess board
    board_color = [pg.Color("white"), (181, 136, 99)]

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


if __name__ == '__main__':
    main()

