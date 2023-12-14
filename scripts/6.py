from functools import reduce
from util import load_input

data = load_input("inputs/6.txt")
times = [int(datum) for datum in data[0].split(":")[1].split(" ") if datum.isdigit()]
distances = [
    int(datum) for datum in data[1].split(":")[1].split(" ") if datum.isdigit()
]

races = list(zip(times, distances))
print(races)


def valid_times(race: tuple[int, int]) -> list[int]:
    res = []
    t, d = race
    for i in range(t):
        travelled = (t - i) * i
        if travelled > d:
            res.append(i)
    return res


results = [valid_times(race) for race in races]
nums = [len(result) for result in results]
print(results)
print(nums)
m = reduce(lambda x, y: x * y, nums)
print(m)

t = int("".join([str(t) for t in times]))
d = int("".join([str(d) for d in distances]))

results = valid_times((t, d))
print(len(results))
