from collections import Counter


def char_counter(ch, path):
    counter_ch = Counter()
    with open(path, 'r') as file:
        for line in file:
            for character in line:
                if ch.match(character):
                    counter_ch[character.upper()] += 1
    characters = [x[0] for x in counter_ch.most_common()]
    characters.sort()
    for i in characters:
        print(i, '-', str(counter_ch[i]))
