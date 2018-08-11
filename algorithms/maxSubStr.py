"""
Given a stream and a set of characters. Get the max substring which contains all
of the given characters.
"""

from collections import defaultdict

def is_hit(count_given, given):
    for ch in given:
        if ch not in count_given:
            return False
    return True

def size(count_given):
    length = 0
    for ch, count in count_given.items():
        length += count
    return length

def main(stream, given):
    count_given = defaultdict(int)

    max_length = 0
    start = -1

    for i, ch in enumerate(stream):
        if ch in given:
            count_given[ch] += 1
        else:
            if is_hit(count_given, given):
                length = size(count_given)
                if length > max_length:
                    max_length = length
                    start = i - max_length
            count_given = defaultdict(int)
        print(start, max_length)
    print(start, max_length)
    return stream[start:start + max_length]


if __name__ == '__main__':
    stream = "this is sample text with xabc abcddy xabcddbcy abb cdxabcd"
    given = ["a", "b", "c", "d"]
    substr = main(stream, given)
    print(substr)
