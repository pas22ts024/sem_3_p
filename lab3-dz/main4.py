import pygame
import sys
import math

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 540, 960
# Количество кадров в секунду
FPS = 60

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Анимация')

# Загрузка изображений
background_img = pygame.image.load('background.png')
starship_img = pygame.image.load('starship.png')
fire_img = pygame.image.load('fire.png')

# Получение размеров фонового изображения
bg_width = background_img.get_width()
bg_height = background_img.get_height()

# Начальные координаты фоновых изображений
bg_y1 = 0
bg_y2 = -bg_height
# Скорость прокрутки фона
bg_speed = 3

# Положение звездолета
starship_rect = starship_img.get_rect()
starship_rect.centerx = WIDTH / 2  # Центрирование по горизонтали

clock = pygame.time.Clock()
time = 0  # Переменная времени для анимации

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновляем переменную времени
    time += 1 / FPS  # Увеличиваем время на долю секунды, равную одному кадру (1/FPS)

    # Вычисляем синусоиду текущего времени
    sine_offset = math.sin(time)  # Значение синуса времени колеблется между -1 и 1
    sine_offset_inverse = 1 - sine_offset  # Инвертированное значение синусоиды для противоположного эффекта

    # Двигаем звездолет по синусоиде вверх-вниз
    starship_rect.y = HEIGHT / 2 + 100 * sine_offset  # Центрируем звездолет и добавляем синусоиду для вертикального движения

    # Обновляем позиции фона для бесконечной прокрутки, изменяя скорость на основе синусоиды
    bg_y1 += bg_speed + 4 * sine_offset_inverse  # Увеличиваем скорость прокрутки фона в зависимости от синусоиды
    bg_y2 += bg_speed + 4 * sine_offset_inverse
    if bg_y1 >= HEIGHT:
        bg_y1 = bg_y2 - bg_height  # Перемещаем фон наверх, если он вышел за нижнюю границу экрана
    if bg_y2 >= HEIGHT:
        bg_y2 = bg_y1 - bg_height  # Перемещаем фон наверх, если он вышел за нижнюю границу экрана

    # Позиция анимации огня под звездолетом
    fire_pos = (starship_rect.centerx - fire_img.get_width() / 2,
                starship_rect.centery + 10 * sine_offset_inverse)  # Положение огня немного смещается по синусоиде

    # Отрисовываем все элементы на экране
    screen.blit(background_img, (0, bg_y1))
    screen.blit(background_img, (0, bg_y2))
    screen.blit(fire_img, fire_pos)
    screen.blit(starship_img, starship_rect.topleft)

    pygame.display.flip()
    clock.tick(FPS)  # Ограничиваем обновление экрана до 60 кадров в секунду
