from util import load_input
from functools import reduce

data = load_input("inputs/2.txt")


def process_games(data: list[str], processing_func) -> int:
    res = 0
    for line in data:
        game_num, cube_data = line.split(":")
        key = game_num.split(" ")[1]
        draws = cube_data.split(";")
        game_results = []
        for draw in draws:
            cubes = {"red": 0, "green": 0, "blue": 0}
            for tally in draw.strip().split(","):
                num, color = tally.strip().split(" ")
                cubes[color] += int(num)
            game_results.append(cubes)
        res += processing_func(int(key), game_results)
    return res


def process_game_1(game_number: int, game_results: list[dict[str, int]]) -> int:
    valid = True
    for result in game_results:
        if result["red"] > 12 or result["green"] > 13 or result["blue"] > 14:
            valid = False
    if valid:
        return game_number
    return 0


def process_game_2(game_number: int, game_results: list[dict[str, int]]) -> int:
    minimums = {"red": 0, "green": 0, "blue": 0}
    for result in game_results:
        for color in ["red", "green", "blue"]:
            minimums[color] = max(minimums[color], result[color])

    return reduce(lambda x, y: x * y, minimums.values())


print(process_games(data, process_game_1))
print(process_games(data, process_game_2))
