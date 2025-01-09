from functools import wraps

import pygame
import random
from pygame.math import Vector2
import numpy 
import copy
import threading

WIDTH = 10
HEIGHT = 10
PIC_UNIT = 20

def print_shape(shape):
    print('------------------print Shape start------------------')
    for i in reversed(range(len(shape))):
        for j in range(len(shape[i])):
            if(shape[i][j]==0):
                print('□ ' ,end='')
            else:
                print('■ ',end='')
        print()
    print('------------------print Shape End------------------')

class BaseGround:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.food = None
        self.ground_data = [[0 for i in range(self.width)] for j in range(self.height)]
        self.create_new_food()

    def create_new_food(self):
        x = random.randint(0, WIDTH - 1)
        y= random.randint(0, HEIGHT - 1)
        self.food = Vector2(x, y)
        pass


class SnakeProxy:
    def __init__(self ,func):
        self._func = func

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            def wrapper(*args, **kwargs):
                print(f"Proxying for {self.name}...")
                instance.lock.acquire()
                result =  self._func(instance, *args, **kwargs)  # 传递 instance
                instance.lock.release()
                return result
            return wrapper

    def __call__(self, func):
        self._func = func
        return self

class MySnake:


    def __init__(self, base_ground: BaseGround):
        self.lock = threading.RLock()
        self.direction = Vector2(1, 0)
        self.head = Vector2(0, 0)
        self.body = [self.head]
        self.ground = base_ground
        self.is_dead = False


    @SnakeProxy
    def move(self):
        new_head = self.head + self.direction
        self.check_dead(new_head)
        if self.is_dead:
            return
        if new_head == self.ground.food:
            self.body.insert(0, new_head)
            self.head = new_head
            self.ground.create_new_food()
            self.move()
        else:
            self.body.insert(0, new_head)
            self.head = new_head
            self.body.remove(self.body[-1])
        pass

    @SnakeProxy
    def check_dead(self,new_head):
        if new_head.x < 0 or new_head.x >= WIDTH or new_head.y < 0 or new_head.y >= HEIGHT:
            self.is_dead = True
            return
        if new_head in self.body[1:]:
            self.is_dead = True
            return

    def print_snake(self):
        print('=============== printSnake ===============')
        print('head:', self.head)
        print('food:', self.ground.food)
        print('is_dead:', self.is_dead)
        ground_copy = copy.deepcopy(self.ground.ground_data)
        for i in range(len(self.body)):
            ground_copy[int(self.body[i].y)][int(self.body[i].x)] = 1
        food = self.ground.food
        ground_copy[int(food.y)][int(food.x)] = 1
        print_shape(ground_copy)
        print('=============== printSnake END ===============')

    def check_direct(self,new_direction):
        if self.direction == new_direction:
            return False
        if self.direction + new_direction == Vector2(0, 0):
            return False
        return True
    @SnakeProxy
    def turn_left(self):
        new_direction = Vector2(-1, 0)
        if self.check_direct(new_direction):
            self.direction = new_direction
        pass
    @SnakeProxy
    def turn_right(self):
        new_direction = Vector2(1, 0)
        if self.check_direct(new_direction):
            self.direction = new_direction
        pass
    @SnakeProxy
    def turn_up(self):
        new_direction = Vector2(0, 1)
        if self.check_direct(new_direction):
            self.direction = new_direction
        pass
    @SnakeProxy
    def turn_down(self):
        new_direction = Vector2(0, -1)
        if self.check_direct(new_direction):
            self.direction = new_direction
        pass


if  __name__ == '__main__':
    ground = BaseGround()
    ground.food = Vector2(2, 0)
    snake = MySnake(ground)
    snake.print_snake()
    snake.move()
    snake.print_snake()
    snake.move()
    snake.print_snake()
    ground.food = Vector2(4, 0)
    snake.move()
    snake.print_snake()
    # snake.turn_up()
    snake.turn_down()
    snake.move()
    snake.print_snake()
    pass