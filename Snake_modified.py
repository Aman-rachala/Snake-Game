import pygame
import time
import random


# Initializing pygame
pygame.init()

#Define Colours
white = (255, 255, 255)   # Snake Colour
black = (0, 0, 0)         # Background Colour
red = (255, 0, 0)         # Game message
orange = (255, 165, 0)    # Food colour

width, height = 600, 400
# Creating a window of size width X height
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aman's Snake Game")

clock = pygame.time.Clock()

snake_size = 15           # Size in pixels
snake_speed = 13          # Speed in pixels/sec

message_font = pygame.font.SysFont('bookmanoldstyle', 30)
score_font = pygame.font.SysFont('bookmanoldstyle', 25)

# Updating the Score after every food collected
def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0,0])      # Score printing position

# Drawing a pixel at pixel[0] of size = snake_size
def draw_snake(snake_size,snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])        

def run_game():
    game_over = False       # To complete the game
    game_close = False      # To Close the game

    x = width / 2
    y = width / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []       # To add multiple Pixels
    snake_length = 1

    target_x = round(random.randrange(15, width - snake_size - 15) / 15) * 15.0
    target_y = round(random.randrange(15, height - snake_size - 15) / 15) * 15.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over!", True, red)
            game_over_message1 = message_font.render("Press 1 to exit", True, red)
            game_over_message2 = message_font.render("Press 2 to play again", True, red)
            game_display.blit(game_over_message, [200, 135])
            game_display.blit(game_over_message1, [200, 170])
            game_display.blit(game_over_message2, [200, 210])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size   # To maintain the speed as 1 block per sec
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed 
        y += y_speed

        game_display.fill(black)
        # Draw the food in orange with snake_size
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])
        
        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]
        
        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True
        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)
        pygame.display.update()
        if x == target_x and y == target_y:
            target_x = round(random.randrange(15, width - snake_size - 15) / 15) * 15.0
            target_y = round(random.randrange(15, height - snake_size - 15) / 15) * 15.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
run_game()