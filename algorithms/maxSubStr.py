"""
Given a stream and a set of characters. Get the max substring which contains all
of the given characters.

The characters can be in any order.
"""

from collections import defaultdict


def is_hit(count_given, given):
    for ch in given:
        if ch not in count_given:
            return False
    return True


def main(stream, given):
    max_length = 0  # max length of matched substring found so far
    count_given = defaultdict(int)
    length = 0
    start = -1  # start index of max substring found so far

    for i, ch in enumerate(stream):  # O(S) => S size of stream.
        if ch in given:
            count_given[ch] += 1
            length += 1
        else:
            if is_hit(count_given, given):
                if length > max_length:
                    max_length = length
                    start = i - length
            count_given = defaultdict(int)
            length = 0
    return stream[start:start + max_length]


if __name__ == '__main__':
    stream = "this is sample abcd text with xabcdas abcddy xabcdrdbcy abb cdxabcd"
    given = ["a", "b", "c", "d"]
    substr = main(stream, given)
    print(substr)
