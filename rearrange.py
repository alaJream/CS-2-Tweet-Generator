import random
from sys import argv as words
# words = ["how", "now", "brown", "cow"]

# random.shuffle(words)
# print(words)

if __name__ == "__main__":
    words.pop(8)
    random.shuffle(words)
    print(words)