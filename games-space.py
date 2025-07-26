import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размер экрана
WIDTH, HEIGHT = 480, 640
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Аркада 70-х: Космический защитник")

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Игрок
player = pygame.Surface((40, 30))
player.fill(GREEN)
player_rect = player.get_rect(center=(WIDTH // 2, HEIGHT - 50))
player_speed = 5

# Пули
bullet = pygame.Surface((4, 10))
bullet.fill(YELLOW)
bullets = []

# Враги
enemy = pygame.Surface((30, 20))
enemy.fill(RED)
enemies = []

def spawn_enemy():
    for i in range(5):
        x = random.randint(0, WIDTH - 30)
        y = random.randint(-150, -40)
        enemies.append(enemy.get_rect(topleft=(x, y)))

spawn_enemy()

# Игровой цикл
running = True
while running:
    clock.tick(FPS)
    win.fill(BLACK)

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed
    if keys[pygame.K_SPACE] and len(bullets) < 5:
        bullets.append(bullet.get_rect(midbottom=player_rect.midtop))

    # Обновление пуль
    for b in bullets[:]:
        b.y -= 10
        if b.bottom < 0:
            bullets.remove(b)

    # Обновление врагов
    for e in enemies[:]:
        e.y += 2
        if e.top > HEIGHT:
            enemies.remove(e)

    # Столкновения
    for e in enemies[:]:
        for b in bullets[:]:
            if e.colliderect(b):
                enemies.remove(e)
                bullets.remove(b)
                break

    # Возвращаем врагов
    if len(enemies) < 5:
        spawn_enemy()

    # Рисуем объекты
    win.blit(player, player_rect)
    for b in bullets:
        win.blit(bullet, b)
    for e in enemies:
        win.blit(enemy, e)

    pygame.display.flip()

pygame.quit()
sys.exit()
