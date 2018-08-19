"""Fibanocci using dynamic programming."""

def fibanocci1(n):
    """simple recursive approach."""
    if n == 0 or n == 1:
        return 1
    else:
        print("compute: {}".format(n))
        return fibanocci1(n-2) + fibanocci1(n - 1)


def fibanocci2(n):
    """memorized dynamic programming approach."""
    cache = {0: 1, 1: 1,}
    def compute(n):
        try:
            result = cache[n]
        except KeyError:
            print("compute: {}".format(n))
            result = compute(n-2) + compute(n-1)
            cache[n] = result
        return result
    return compute(n)

if __name__ == '__main__':
    print(fibanocci1(5))
    print("...")
    print(fibanocci2(5))

