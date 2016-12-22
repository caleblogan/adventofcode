INPUT_FNAME = 'res/day8_inp.txt'

def read_input():
    res = []
    with open(INPUT_FNAME, 'r') as fh:
        for line in fh:
            res.append(line.strip())
    return res

def print_screen(grid):
    for row in grid:
        for col in row:
            if col:
                print('#', end='')
            else:
                print('.', end='')
        print('')

def build_grid(width, height):
    grid = []
    for row in range(height):
        grid.append([])
        for col in range(width):
            grid[row].append(0)
    return grid

def fill_rect(grid, a, b):
    """Fill a grid axb starting at Top Left (0, 0)"""
    for col in range(a):
        for row in range(b):
            grid[row][col] = 1

def rotate_row(grid, row, n):
    """Rotates a row down wrapping around"""
    cash = []
    for col in grid[row]:
        cash.append(col)
    for i, elem in enumerate(cash):
        i = (i + n) % len(grid[row])
        grid[row][i] = elem

def rotate_col(grid, col, n):
    """Roates a col to the right wrapping around."""
    cash = []
    for row in grid:
        cash.append(row[col])
    for i, elem in enumerate(cash):
        i = (i + n) % len(grid)
        grid[i][col] = elem

def tokenize_instruction(instruction):
    tokens = [token.strip() for token in instruction.split(' ')]
    return tokens

def parse_fill_instruction(tokens):
    a, b = tokens[1].split('x')
    return int(a), int(b)

def parse_rotate_instruction(tokens):
    row_col = tokens[2].split('=')[1].strip()
    n = tokens[4].strip()
    return int(row_col), int(n)

def handle_instruction(grid, instruction):
    tokens = tokenize_instruction(instruction)
    if tokens[0] == 'rect':
        a, b = parse_fill_instruction(tokens)
        fill_rect(grid, a, b)
    elif tokens[0] == 'rotate' and tokens[1] == 'column':
        col, n = parse_rotate_instruction(tokens)
        rotate_col(grid, col, n)
    elif tokens[0] == 'rotate' and tokens[1] == 'row':
        row, n = parse_rotate_instruction(tokens)
        rotate_row(grid, row, n)

def sum_pixels(screen):
    count = 0
    for row in screen:
        for col in row:
            if col is 1:
                count += 1
    return count

def main():
    instructions = read_input()
    screen = build_grid(50, 6)
    for instruction in instructions[:]:
        handle_instruction(screen, instruction)
    print_screen(screen)
    print('Number of Pixel On:', sum_pixels(screen))

def test():
    screen = build_grid(7, 3)
    fill_rect(screen, 3, 2)
    rotate_col(screen, 1, 1)
    rotate_row(screen, 0, 4)
    rotate_col(screen, 1, 1)

if __name__ == '__main__':
    main()
