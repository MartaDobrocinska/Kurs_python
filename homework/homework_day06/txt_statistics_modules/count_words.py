from collections import Counter


def count_words(text):
    text = text.lower()
    convert = [".", ", ", ":", ";", "'", '"']
    for i in convert:
        text = text.replace(i, "").replace("\n", " ").replace("\r", "")
    word_count = Counter(text.split(" "))
    blank = word_count['']
    print("Liczba wyrazów:", sum(word_count.values()) - blank)
    print("Liczba unikatowych wyrazów:", len(word_count) - blank)
