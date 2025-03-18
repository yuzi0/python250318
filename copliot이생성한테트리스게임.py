#cmd
#pip install pygame
import pygame
import random

# 게임 설정
pygame.init()
screen_width = 300
screen_height = 600
block_size = 30
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# 색상 정의
colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (128, 0, 128)
]

# 테트리스 블록 모양
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [1, 0, 0]]
]

class Tetris:
    def __init__(self, screen):
        self.screen = screen
        self.board = [[0 for _ in range(screen_width // block_size)] for _ in range(screen_height // block_size)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.game_over = False
        self.score = 0

    def new_piece(self):
        return [random.choice(shapes), random.randint(0, len(colors) - 1)]

    def draw_board(self):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                pygame.draw.rect(self.screen, colors[cell], (x * block_size, y * block_size, block_size, block_size), 0)

    def draw_piece(self, piece, offset):
        shape, color = piece
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, colors[color], ((off_x + x) * block_size, (off_y + y) * block_size, block_size, block_size), 0)

    def valid_move(self, piece, offset):
        shape, _ = piece
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if x + off_x < 0 or x + off_x >= screen_width // block_size or y + off_y >= screen_height // block_size:
                        return False
                    if self.board[y + off_y][x + off_x]:
                        return False
        return True

    def freeze_piece(self, piece, offset):
        shape, color = piece
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[y + off_y][x + off_x] = color
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        if not self.valid_move(self.current_piece, (5, 0)):
            self.game_over = True

    def clear_lines(self):
        new_board = [row for row in self.board if any(cell == 0 for cell in row)]
        lines_cleared = len(self.board) - len(new_board)
        self.board = [[0 for _ in range(screen_width // block_size)] for _ in range(lines_cleared)] + new_board
        self.score += lines_cleared

    def run(self):
        clock = pygame.time.Clock()
        piece_x, piece_y = 5, 0
        while not self.game_over:
            self.screen.fill((0, 0, 0))
            self.draw_board()
            self.draw_piece(self.current_piece, (piece_x, piece_y))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.valid_move(self.current_piece, (piece_x - 1, piece_y)):
                        piece_x -= 1
                    elif event.key == pygame.K_RIGHT and self.valid_move(self.current_piece, (piece_x + 1, piece_y)):
                        piece_x += 1
                    elif event.key == pygame.K_DOWN and self.valid_move(self.current_piece, (piece_x, piece_y + 1)):
                        piece_y += 1
                    elif event.key == pygame.K_UP:
                        self.current_piece[0] = list(zip(*self.current_piece[0][::-1]))
                        if not self.valid_move(self.current_piece, (piece_x, piece_y)):
                            self.current_piece[0] = list(zip(*self.current_piece[0]))[::-1]
            if not self.valid_move(self.current_piece, (piece_x, piece_y + 1)):
                self.freeze_piece(self.current_piece, (piece_x, piece_y))
                piece_x, piece_y = 5, 0
            else:
                piece_y += 1
            clock.tick(5)  # 블록이 천천히 떨어지도록 수정

if __name__ == "__main__":
    game = Tetris(screen)
    game.run()
    pygame.quit()