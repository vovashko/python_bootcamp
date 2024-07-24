with open ('input.txt', 'r') as file:
    data = file.readlines()

cubes_rules = {'red' : '12',
                'blue' : '14',
                'green' : '13'}

def check_cubes (input_string):
    game_id = 0
    game_str, cubes_combinations = input_string.split(':')
    cubes_sets = cubes_combinations.split(';')
    sets_are_valid = True
    for cubes_in_one_set in cubes_sets:
        cube_count = {'red' : 0, 'blue' : 0, 'green' : 0}
        for cube in cubes_in_one_set.split(','):
            cube = cube.strip()
            if cube:
                count, color = cube.split(' ')
                count = int(count)
                if color in cube_count:
                    cube_count[color] += count    
        for color, count in cube_count.items():
            if count > int(cubes_rules[color]):
                sets_are_valid = False
                break
   
    if sets_are_valid == True:
        game_id = ''.join([char for char in game_str.strip() if char.isdigit()])
    else:
        game_id = 0
    return int(game_id)

i = 0
answer = 0

while i < len(data):
    input_string = data[i].strip()
    games = check_cubes(input_string)
    answer += games
    i += 1

print(f"Answer: {answer}")