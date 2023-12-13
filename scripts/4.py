from util import load_input

data = load_input("inputs/4.txt")


def process_card(card: str) -> int:
    sets = []
    for s in card.split(":")[1].split("|"):
        a = s.replace("  ", " ")
        a = a.strip().split(" ")
        sets.append(set(a))
    overlap = sets[0].intersection(sets[1])
    return len(overlap)


res = 0
for line in data:
    num_winning = process_card(line)
    if num_winning == 0:
        continue
    res += 1 << (max(0, num_winning - 1))

print(res)


cards_processed = 0
cards_to_process = list(range(len(data)))
memo = dict()
while len(cards_to_process) > 0:
    cards_processed += 1
    card_num = cards_to_process.pop()
    if card_num in memo:
        score = memo[card_num]
    else:
        score = process_card(data[card_num])
        memo[card_num] = score
    cards_to_process += list(range(card_num + 1, card_num + score + 1))

print(cards_processed)
