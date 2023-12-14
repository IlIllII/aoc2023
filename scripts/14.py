from util import load_input

data = load_input("inputs/14.txt")

data = [[char for char in line] for line in data]


def swap(pos1, pos2, data):
    data[pos1[1]][pos1[0]], data[pos2[1]][pos2[0]] = (
        data[pos2[1]][pos2[0]],
        data[pos1[1]][pos1[0]],
    )


def rotated_data(data):
    new_data = []
    for x in range(len(data[0])):
        new_row = []
        for y in range(len(data), 0, -1):
            new_row.append(data[y - 1][x])
        new_data.append(new_row)
    return new_data


def tilt(data):
    for _ in range(len(data)):
        for x in range(len(data[0])):
            for y in range(len(data)):
                if y + 1 < len(data):
                    if data[y][x] == "." and data[y + 1][x] == "O":
                        swap((x, y), (x, y + 1), data)
    return data


def tilt2(data):
    for x in range(len(data[0])):
        for y in range(len(data)):
            if data[y][x] == "O":
                y2 = y - 1
                while y2 >= 0:
                    if data[y2][x] != ".":
                        break
                    y2 -= 1

                y2 += 1
                swap((x, y), (x, y2), data)
    return data


def cycle(data):
    for _ in range(4):
        data = tilt2(data)
        data = rotated_data(data)
    return data


def copy_board(data):
    new_data = []
    for row in data:
        new_data.append([char for char in row])
    return new_data


def compare_boards(data1, data2):
    for y in range(len(data1)):
        for x in range(len(data1[0])):
            if data1[y][x] != data2[y][x]:
                return False
    return True


def count(data):
    total = 0
    for i, row in enumerate(reversed(data)):
        for char in row:
            if char == "O":
                total += i + 1
    return total


end = 1000000000

while end > 176:
    end = end - 44

print(end)


for i in range(1000000000):
    if i % 10000 == 0:
        data_copy = copy_board(data)
        data = cycle(data)
        print("boards equal:", compare_boards(data_copy, data))
        print(i, "/")
        print(1000000000)
        print("Count: ", count(data))
    else:
        data = cycle(data)
    print("Count: ", count(data), i)
    if i == 163:
        print("FOUND IT: ", count(data), i)

print(count(data))
