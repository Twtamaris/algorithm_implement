import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
OBSTACLE_SIZE = 10
GATE_WIDTH = 10

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def initialize_grid():
    maze_coordinates = []
    for y in range(HEIGHT//OBSTACLE_SIZE):
        maze_coordinates.append([0 for x in range(WIDTH//OBSTACLE_SIZE)])
    return maze_coordinates

def generate_maze(x, y, grid):
    # Mark garney current cell visit gareko bhanera
    grid[y][x] = 1 
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left
    random.shuffle(directions)
    
    for dx, dy in directions:
        new_x, new_y = x + dx * 2, y + dy * 2  # Jump 2 steps to the next cell
        
        if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] == 0:
            grid[(y + dy)][(x + dx)] = 1
            generate_maze(new_x, new_y, grid)

def create_obstacles(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                pygame.draw.rect(screen, WHITE, (x * OBSTACLE_SIZE, y * OBSTACLE_SIZE, OBSTACLE_SIZE, OBSTACLE_SIZE))

def create_boundary():
    pygame.draw.rect(screen, RED, (0, 0, WIDTH, GATE_WIDTH))  # Top
    pygame.draw.rect(screen, RED, (0, HEIGHT - GATE_WIDTH, WIDTH, GATE_WIDTH))  # Bottom
    pygame.draw.rect(screen, RED, (0, 0, GATE_WIDTH, HEIGHT))  # Left
    pygame.draw.rect(screen, RED, (WIDTH - GATE_WIDTH, 0, GATE_WIDTH, HEIGHT))  # Right

def snake(grid):
    pygame.draw.rect(screen, RED, (0, 0, OBSTACLE_SIZE, OBSTACLE_SIZE))

def snake_up_down_moves(grid, pos):
    valid_moves = []
    direction = [(0, -1), (0, 1) , (1, 0), (-1, 0)]

    for dx, dy in direction:
        new_x, new_y = pos[0] + dx, pos[1] + dy
        if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] == 0:
            valid_moves.append((new_x, new_y))
    return valid_moves


def main():
    grid = initialize_grid()
    generate_maze(0, 0, grid)
    snake_position = [(0, 0)]


    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # draw the maze
        create_obstacles(grid)
        # create_boundary()

        snake(grid)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
