import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Штурмовик мишень.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Скорость движения мишени
target_speed_x = 0.1  # Скорость по оси X
target_speed_y = 0.1  # Скорость по оси Y

# Переменная для подсчета очков
score = 0

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
           mouse_x, mouse_y = pygame.mouse.get_pos()
           if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
              score += 1  # Увеличиваем счет на 1
              target_x = random.randint(0, SCREEN_WIDTH - target_width)
              target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    # Движение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка границ экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
       target_speed_x = -target_speed_x  # Изменение направления по оси X
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
       target_speed_y = -target_speed_y  # Изменение направления по оси Y

    screen.blit(target_img, (target_x, target_y))

    # Отображение счета
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))  # Белый цвет текста
    screen.blit(score_text, (10, 10))  # Позиция текста на экране

    pygame.display.update()

pygame.quit()