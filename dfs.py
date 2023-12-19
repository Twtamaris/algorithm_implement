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




def snake(grid, snake_pos):
    # Draw the head of the snake in red
    pygame.draw.rect(screen, RED, (snake_pos[0] * OBSTACLE_SIZE, snake_pos[1] * OBSTACLE_SIZE, OBSTACLE_SIZE, OBSTACLE_SIZE))
    
    


def move_snake(grid, snake_pos, snake_visited):
    direction = [(0, -1), (0, 1) , (1, 0), (-1, 0)]
    snake_vistied.append(snake_pos)
    print(snake_visited)

    
    snake_visited.append(snake_pos)
    random.shuffle(direction)
    for dx, dy in direction:
        new_x, new_y = snake_pos[0] + dx, snake_pos[1] + dy
        if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] == 1:
            if (new_x, new_y) not in snake_visited:
                print("new_x, new_y", new_x, new_y)
                snake_visited.pop(0)
                # print(visited)
                return (new_x, new_y)
    return snake_pos



            
            
        
    

snake_vistied = []

def main():
    grid = initialize_grid()
    generate_maze(0, 0, grid)
    snake_position = (0,0)

    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        create_obstacles(grid)  # Draw the maze obstacles first
        snake_position = move_snake(grid, snake_position, snake_vistied)  # Update snake position after drawing
        snake(grid, snake_position)  # Draw the snake on top of the maze


        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
