import random

NEIGHBOURS_COORDS = [
  (0, -1),  # UP
  (1, -1),  # UP_RIGHT
  (1, 0),   # RIGHT
  (1, 1),   # DOWN_RIGHT
  (0, 1),   # DOWN
  (-1, 1),  # DOWN_LEFT
  (-1, 0),  # LEFT
  (-1, -1), # UP_LEFT
]

def generate_grid(size: int) -> dict:
  grid = {}
  for x in range(0, size):
    grid[x] = {}
    for y in range(0, size):
      grid[x][y] = bool(random.randint(-1, 1))
  return grid

def get_live_neighbours_count(grid: dict, x: int, y: int) -> int:
  count = 0
  size = len(grid)
  for (offset_x, offset_y) in NEIGHBOURS_COORDS:
    nx = x + offset_x
    ny = y + offset_y
    if nx >= 0 and nx < size and ny >=0 and ny < size and grid[nx][ny]:
      count += 1

  return count

def run_tick(grid: dict) -> None:
  size = len(grid)
  for x in range(0, size):
    for y in range(0, size):
      live_neighbours_count = get_live_neighbours_count(grid, x, y)

      if grid[x][y]:
        if live_neighbours_count < 2 or  live_neighbours_count > 3:
          grid[x][y] = False
      elif live_neighbours_count == 3:
        grid[x][y] = True