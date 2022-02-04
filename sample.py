import sys
import random


if len(sys.argv) < 2:
    sys.exit(0)

words = None

if len(sys.argv) == 2:
    f = open(sys.argv[1], 'r')
    words = f.readline()

random.shuffle(words)

print(words[0])
