with open ('input.txt', 'r') as file:
    data = file.readlines()

def check_cubes (input_string):
    power = 0
    game_str, cubes_combinations = input_string.split(':')
    cubes_sets = cubes_combinations.split(';')
    sets_are_valid = True
    cube_count = {'red' : 0, 'blue' : 0, 'green' : 0}
    for cubes_in_one_set in cubes_sets:
        for cube in cubes_in_one_set.split(','):
            cube = cube.strip()
            if cube:
                count, color = cube.split(' ')
                count = int(count)
                if color in cube_count and count > cube_count[color]:
                    cube_count[color] = count    
    print(f"{game_str} Cube count: {cube_count}")
   
    power = cube_count['red'] * cube_count['blue'] * cube_count['green']
    return power

i = 0
answer = 0

while i < len(data):
    input_string = data[i].strip()
    games = check_cubes(input_string)
    answer += games
    i += 1

print(f"Answer: {answer}")