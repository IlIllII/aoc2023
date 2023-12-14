from util import load_input


inputs, *blocks = open("inputs/5.txt").read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

result = 10000000000000000000
ranges = []
for block in reversed(blocks):
    single_ranges = []
    for line in block.splitlines()[1:]:
        single_ranges.append(list(map(int, line.split())))
    single_ranges.sort(key=lambda x: x[0])
    ranges.append(single_ranges)

for i, loc in enumerate(range(100000000)):
    seed = -1
    r_idx = 0
    try:
        seed = loc
        while r_idx < len(ranges):
            found = False
            for r2 in ranges[r_idx]:
                if r2[0] <= seed < r2[0] + r2[2]:
                    delta = seed - r2[0]
                    seed = r2[1] + delta
                    r_idx += 1
                    found = True
                    break
            if not found:
                r_idx += 1
        if r_idx != len(ranges):
            raise ValueError("Not in range")
    except:
        continue

    if seed != -1:
        for seed_range in seeds:
            if seed_range[0] <= seed <= seed_range[1]:
                result = min(loc, result)
                break
print("result: " + str(result))


class RangeMap:
    def __init__(self, ranges: list[list[int]]) -> None:
        self.ranges = ranges

    def translate_value(self, value: int) -> int:
        for dest, src, length in self.ranges:
            if src <= value <= src + length:
                delta = value - src
                return dest + delta
        return value

    def reverse_translate(self, value: int) -> int:
        for dest, src, length in reversed(self.ranges):
            if dest <= value <= dest + length:
                delta = value - dest
                return src + delta
        raise ValueError("Value not in range map")

    def __repr__(self) -> str:
        return "RangeMap" + str(self.ranges)


data = load_input("inputs/5.txt")

line_num = 0
seeds = []

maps = [[], [], [], [], [], [], []]
map_idx = 0

while line_num < len(data):
    if data[line_num] == "":
        map_idx += 1
        line_num += 1
        continue
    if data[line_num].startswith("seeds"):
        line = data[line_num].split(":")[1].strip().split(" ")
        seeds += [int(seed) for seed in line]
        map_idx -= 1
    if data[line_num][0].isdigit():
        line = data[line_num].strip().split(" ")
        maps[map_idx].append([int(num) for num in line])
    line_num += 1

range_maps = []

for i, m in enumerate(maps):
    range_maps.append(RangeMap(m))


minimum = 100000000000000000000000000
for seed in seeds:
    val = seed
    for range_map in range_maps:
        val = range_map.translate_value(val)
    minimum = min(minimum, val)

print(minimum)