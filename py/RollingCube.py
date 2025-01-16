import pygame
import numpy as np
import time

# 初始化 Pygame
pygame.init()

# 屏幕尺寸
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("旋转立方体")

# 颜色
WHITE = (0, 255, 0)
BLACK = (0, 0, 0)

# 立方体参数
cube_size = 4
cube_edge_length = 50  # 每个小立方体的边长
cube_center = np.array([WIDTH / 2, HEIGHT / 2, 0])

# 定义立方体的所有顶点
vertices = []
for x in range(cube_size):
    for y in range(cube_size):
        for z in range(cube_size):
            vertices.append(np.array([x * cube_edge_length, y * cube_edge_length, z * cube_edge_length]))
vertices = np.array(vertices)

# 定义立方体的所有边 (连接顶点的线)
edges = []
for i in range(cube_size**3):
    x, y, z = i % cube_size, (i // cube_size) % cube_size, i // (cube_size**2)
    for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < cube_size and 0 <= ny < cube_size and 0 <= nz < cube_size:
            ni = nx + ny * cube_size + nz * cube_size**2
            if ni > i: #避免重复线段
                edges.append((i, ni))

edges = np.array(edges)

def rotate_x(angle):
    """绕 X 轴旋转的矩阵"""
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]
    ])

def rotate_y(angle):
    """绕 Y 轴旋转的矩阵"""
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]
    ])

def rotate_z(angle):
    """绕 Z 轴旋转的矩阵"""
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1]
    ])
# 初始旋转角度（弧度）
initial_x_angle = np.pi / 6  # 30 度
initial_y_angle = np.pi / 4  # 45 度
initial_z_angle = np.pi / 3  # 60 度

# 旋转角度和速度
angle = 0
rotation_speed = np.pi / 4  # 每秒 45 度

last_time = time.time()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 计算时间差
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time

    # 更新旋转角度
    angle += rotation_speed * delta_time

    # 清空屏幕
    screen.fill(BLACK)

    # 旋转并投影顶点
    rotated_vertices = vertices - (cube_size-1) * cube_edge_length / 2 # 将中心移到原点

    # 应用初始旋转
    rotated_vertices = rotated_vertices @ rotate_x(initial_x_angle)
    rotated_vertices = rotated_vertices @ rotate_y(initial_y_angle)
    rotated_vertices = rotated_vertices @ rotate_z(initial_z_angle)

    rotated_vertices = rotated_vertices @ rotate_x(angle) # 旋转
    rotated_vertices = rotated_vertices + cube_center # 移回原位

    # 绘制立方体的边
    for edge in edges:
        start_vertex = rotated_vertices[edge[0]][:2].astype(int)
        end_vertex = rotated_vertices[edge[1]][:2].astype(int)
        pygame.draw.line(screen, WHITE, start_vertex, end_vertex, 2)

    # 更新显示
    pygame.display.flip()

pygame.quit()