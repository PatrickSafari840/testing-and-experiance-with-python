import random
import time
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define snake size and speed
snake_block = 10
snake_speed = 15


def draw_snake(snake_list):
    """Draws the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    """Displays a message on the screen."""

    font_style = pygame.font.SysFont(None, 30)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def game_loop():
    """The main game loop."""
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_speed:
                    x1_change = -snake_speed
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_speed:
                    x1_change = snake_speed
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_speed:
                    y1_change = -snake_speed
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_speed:
                    y1_change = snake_speed
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_list)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

        clock.tick(snake_speed)

        if game_close:
            screen.fill(BLACK)
            message("You Lost! Press P to Play Again or Q to Quit", RED)
            pygame.display.update()

            while game_close:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            game_loop()
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False  # Ensure to exit the close loop as well

    pygame.quit()
    quit()
