import random
from distutils.command.clean import clean
from pprint import pprint

def histogram(source_text):
    with open(source_text, 'r') as f:
        source = f.read().lower()
        split_source = source.split()
        hist = {}
        for word in split_source:
            clean_word = word.strip("""'",♪..:--"?!();""")
            if clean_word in hist:
                hist[clean_word] += 1
            else:
                hist[clean_word] = 1
        return hist

def unique_words(histogram):
    return len(histogram.keys())

def frequency(word, histogram):
    return histogram[word]

hist = histogram('')
pprint(hist)
print(unique_words(hist))
def random_word(hist):
    return random.choice(list(hist.keys()))

print(random_word(hist))