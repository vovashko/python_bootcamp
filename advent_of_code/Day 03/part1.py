with open ('example.txt', 'r') as file:
    data = file.readlines()

def check_if_symbol (cell):
    if cell == '.' or cell.isdigit():
        return False
    return True

def check_adjacent(grid, row, col):
    directions = [(-1,-1), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1)]
    adjacent = []
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
            adjacent.append(grid[new_row][new_col])
    return adjacent

def sum_num_parts (grid):
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col].isdigit():
                adjacent = check_adjacent(grid, row, col)
                if any([check_if_symbol(cell) for cell in adjacent]):
                    total += int(grid[row][col])

    return total

grid = [list(row.strip()) for row in data] 

print(f"Answer: {sum_num_parts(grid)}")
    