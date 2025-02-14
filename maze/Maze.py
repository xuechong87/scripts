import pygame
import random
import numpy
import copy
from pygame import Vector2

WIDTH = 30
HEIGHT = 30
PIC_UNIT = 8
WALL_COLOR = (0,180,0)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

vector_to_rect = lambda v: pygame.Rect(v.x * PIC_UNIT, v.y * PIC_UNIT, PIC_UNIT, PIC_UNIT)

def draw_vector(surface, vector, color):
    pygame.draw.rect(surface, color, vector_to_rect(vector), PIC_UNIT)

def print_shape(shape):
    print('------------------print Shape start------------------')
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]==0:
                print('□ ' ,end='')
            elif shape[i][j]==-1:
                print('★ ',end='')
            else:
                print('■ ',end='')
        print()
    print('------------------print Shape End------------------')


class BaseGround:

    def __init__(self):
        self.width = WIDTH + 2
        self.height = HEIGHT + 2
        self.start = Vector2(1, 1)
        self.end = Vector2(WIDTH, HEIGHT)

        self.ground_data = [[1 for i in range(self.width)] for j in range(self.height)]

    def print_ground(self):
        print_shape(self.ground_data)

    def draw(self,surface):
        self.print_ground()
        for i in range(self.height):
            for j in range(self.width):
                if self.ground_data[i][j] == 1:
                    pygame.draw.rect(surface, WALL_COLOR, (j*PIC_UNIT, i*PIC_UNIT, PIC_UNIT, PIC_UNIT))
        pygame.draw.rect(surface, RED, vector_to_rect(self.start), 0)
        pygame.draw.rect(surface, BLUE, vector_to_rect(self.end), 0)


    def generate(self):
        # 迷宫生成算法（这里使用简单的随机算法）
        for i in range(1, HEIGHT +1):
            for j in range(1, WIDTH +1):
                if random.random() < 0.3:
                    self.ground_data[i][j] = 1  # 设置为墙壁
                else:
                    self.ground_data[i][j] = 0

        self.after_generate()

    #设置出口和入口为可通过
    def after_generate(self):
        self.ground_data[int(self.start.x)][int(self.start.y)] = 0
        self.ground_data[int(self.end.x)][int(self.end.y)] = 0

    #检查当前点是否有墙或超出界限
    def have_wall(self,point):

        if point.x < 1 or point.x >= WIDTH +1 or point.y < 1 or point.y >= HEIGHT+1:
            return True
        if self.ground_data[int(point.x)][int(point.y)] == 1:
            return True
        return False

    '''检查迷宫是否有解'''
    def check_maze(self):
        walk_path = []
        visited = set()  # 记录已访问的格子

        def dfs(point):
            if point == self.end:  # 到达终点
                return True

            walk_path.append(point)
            visited.add(point.as_polar())

            directions = [Vector2(0, 1), Vector2(0, -1), Vector2(1, 0), Vector2(-1, 0)]
            random.shuffle(directions)  # 随机打乱方向

            for d in directions:
                next_point = point + d
                if not self.have_wall(next_point) and next_point.as_polar() not in visited:
                    if dfs(next_point):
                        return True
            walk_path.pop()  # 回溯
            return False

        start_point = self.start

        result =dfs(start_point)

        print("check_maze:",result)

        return result, walk_path

    def walk(self, surface):

        (result, route) = self.check_maze()
        if not result:
            print("no route")

        route_shape = self.route_shape(route)
        print_shape(route_shape)
        for v in route:
            draw_vector(surface,v,WHITE)
        pass

    def route_shape(self,route):
        ground_copy = copy.deepcopy(self.ground_data)
        for v in route:
            ground_copy[int(v.x)][int(v.y)] = -1
        return ground_copy


if __name__ == '__main__':
    ground = BaseGround()
    ground.generate()
    ## 用pygame画图
    pygame.init()
    screen = pygame.display.set_mode(((WIDTH+2)*PIC_UNIT, (HEIGHT+2)*PIC_UNIT))
    screen.fill(BLACK)

    pygame.display.set_caption("MAZE")

    ground.draw(screen)
    ground.walk(screen)

    pygame.display.update()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)
