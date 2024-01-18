import click
import time
from conway import generate_grid, run_tick

ALIVE_CELL_CHAR = '⬜'
DEAD_CELL_CHAR = '⬛'

def render_grid(grid: dict) -> str:
  output = ''
  size = len(grid)
  for x in range(0, size):
    for y in range(0, size):
      if grid[x][y]:
        output += ALIVE_CELL_CHAR
      else:
        output += DEAD_CELL_CHAR
    output += '\n'
  return output

@click.group()
def cli():
  pass

@cli.command()
@click.option('--grid-size', type=int, default=30)
@click.option('--tick-interval', type=float, default=1)
def simulate(grid_size: int = 30, tick_interval = 1):
  grid = generate_grid(grid_size)
  tick = 0

  click.clear()
  click.echo(render_grid(grid))

  while (True):
    tick += 1
    run_tick(grid)

    click.clear()
    click.echo(render_grid(grid))

    time.sleep(tick_interval)

if __name__ == '__main__':
  cli()