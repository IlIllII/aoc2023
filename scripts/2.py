from util import load_input

data = load_input('inputs/2.txt')

def process_games(data: list[str]) -> int:
    res = 0
    for line in data:
        game_num, cube_data = line.split(":")
        key = game_num.split(" ")[1]
        draws = cube_data.split(";")
        valid = True
        for draw in draws:
            cubes = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            for tally in draw.strip().split(","):
                num, color = tally.strip().split(" ")
                cubes[color] += int(num)
            if cubes["red"] > 12 or cubes["green"] > 13 or cubes["blue"] > 14:
                valid = False
        if valid:
            res += int(key)
    return res

print(process_games(data))

