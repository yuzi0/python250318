#chatgpt로 생성한 블록깨기

import pygame
import random

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록 깨기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLACK = (0, 0, 0)

# 패들 설정
paddle_width, paddle_height = 100, 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 40
paddle_speed = 7

# 공 설정
ball_radius = 8
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 4, -4

# 블록 설정
block_rows, block_cols = 5, 8
block_width = WIDTH // block_cols
block_height = 30
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        blocks.append(pygame.Rect(col * block_width, row * block_height + 50, block_width - 2, block_height - 2))

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed
    
    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # 벽 충돌
    if ball_x <= 0 or ball_x >= WIDTH - ball_radius * 2:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y
    
    # 패들 충돌
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle_rect.colliderect((ball_x, ball_y, ball_radius * 2, ball_radius * 2)):
        ball_speed_y = -ball_speed_y
    
    # 블록 충돌
    for block in blocks[:]:
        if block.colliderect((ball_x, ball_y, ball_radius * 2, ball_radius * 2)):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y
            break
    
    # 게임 종료 조건
    if ball_y >= HEIGHT:
        print("게임 오버!")
        running = False
    elif not blocks:
        print("게임 클리어!")
        running = False
    
    # 그리기
    pygame.draw.rect(screen, BLUE, paddle_rect)
    pygame.draw.ellipse(screen, RED, (ball_x, ball_y, ball_radius * 2, ball_radius * 2))
    for block in blocks:
        pygame.draw.rect(screen, GREEN, block)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
