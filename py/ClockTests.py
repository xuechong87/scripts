import pygame
import MySnake
from MySnake import WIDTH,HEIGHT, PIC_UNIT

pygame.init()

clock = pygame.time.Clock()

running = True

ground = MySnake.BaseGround()
snake = MySnake.MySnake(ground)

width, height = (WIDTH + 10 ) * PIC_UNIT, (HEIGHT + 10) * PIC_UNIT
screen = pygame.display.set_mode((width, height))

move_interval = 800
last_move_time = pygame.time.get_ticks()

while running:
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    print('tick')



    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print('key down:', event.key)
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                snake.turn_left()
            if event.key == pygame.K_RIGHT:
                snake.turn_right()
            if event.key == pygame.K_UP:
                snake.turn_up()
            if event.key == pygame.K_DOWN:
                snake.turn_down()
    
    if current_time - last_move_time > move_interval:
        snake.move()
        snake.print_snake()
        last_move_time = current_time

    snake.draw(screen)
    pygame.display.flip()
    # pygame.time.delay(1000)

pygame.quit()