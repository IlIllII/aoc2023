from util import load_input


with open("inputs/13.txt", "r") as f:
    code = f.read()

patterns = code.split("\n\n")
res = []
for pattern in patterns:
    rows = pattern.split("\n")
    for i in range(len(rows)):
        flaws_found = 0
        valid = True
        found_edge = False
        offset = 0
        while not found_edge:
            if i + offset >= len(rows):
                break
            elif i - offset - 1 < 0:
                break
            elif not valid:
                break
            else:
                for j in range(len(rows[0])):
                    if rows[i + offset][j] != rows[i - offset - 1][j]:
                        flaws_found += 1
                        if flaws_found > 1:
                            valid = False
                            break
            offset += 1
        if valid and i != 0 and flaws_found == 1:
            res.append(i * 100)
            break


    columns = []
    for i in range(len(rows[0])):
        columns.append("".join([row[i] for row in rows]))
    rows = columns
    for i in range(len(rows)):
        flaws_found = 0
        valid = True
        found_edge = False
        offset = 0
        while not found_edge:
            if i + offset >= len(rows):
                break
            elif i - offset - 1 < 0:
                break
            elif not valid:
                break
            else:
                for j in range(len(rows[0])):
                    if rows[i + offset][j] != rows[i - offset - 1][j]:
                        flaws_found += 1
                        if flaws_found > 1:
                            valid = False
                            break
            offset += 1
        if valid and i != 0 and flaws_found == 1:
            res.append(i)
            break

print(sum(res))