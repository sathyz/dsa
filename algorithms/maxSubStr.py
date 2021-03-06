"""
Given a stream and a set of characters. Get the max substring which contains
all of the given characters.

The characters can be in any order.
"""
from collections import Counter


def is_hit(counter, given):
    for ch in given:
        if ch not in counter:
            return False
    return True


def preprocess(stream, given):
    substr = []
    count_given = Counter()
    for ch in stream:
        if ch in given:
            substr.append(ch)
            count_given[ch] += 1
        elif substr:
            if is_hit(count_given, given):
                yield "".join(substr)
            substr = []
            count_given = Counter()


def main(stream, given):
    max_length = 0
    res = None
    for substr in preprocess(stream, given):
        length = len(substr)
        if length > max_length:
            max_length = length
            res = substr
    return res


if __name__ == '__main__':
    stream = """this is sample abcd text with xabccas abcddy xabcdrdbcy abb
cdxabcd. defcabddca zxdddacccb ghf bbbcddddkkkkl lijabcdfg."""
    given = ["a", "b", "c", "d"]
    substr = main(stream, given)
    print(substr)
