from functools import reduce
from util import load_input

data = load_input("inputs/3.txt")

symbol_indices = []
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if not char.isdigit() and char != ".":
            symbol_indices.append((x, y))


def nearby_numbers(data: list[str], x: int, y: int) -> list[int]:
    visited = set()
    res = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if x + i < 0 or x + i >= len(data[0]):
                continue
            if y + j < 0 or y + j >= len(data):
                continue
            if data[y + j][x + i].isdigit():
                start_idx = x + i
                while data[y + j][start_idx].isdigit():
                    start_idx -= 1
                    if start_idx < 0:
                        break
                start_idx += 1
                end_bound = start_idx
                while data[y + j][end_bound].isdigit():
                    end_bound += 1
                    if end_bound >= len(data[y + j]):
                        break
                ii = int(data[y + j][start_idx:end_bound])
                if ii in visited:
                    continue
                visited.add(ii)
                res.append(ii)
    return res


def find_gear_ratios(data: list[int]) -> int:
    if len(data) < 2:
        return 0
    else:
        return reduce(lambda x, y: x * y, data)


results = []
for x, y in symbol_indices:
    results += nearby_numbers(data, x, y)

print(sum(results))

gear_ratios = 0
for x, y in symbol_indices:
    if data[y][x] == "*":
        gear_ratios += find_gear_ratios(nearby_numbers(data, x, y))

print(gear_ratios)
