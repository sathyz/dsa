def multiply(a, b):
    """
>>> multiply("1234", "12")
      1234 x
        12
------------
      2468 +
     12340 +
------------
     14808
------------
    """
    print("{:>10} x".format(a))
    print("{:>10}".format(b))
    print("-" * 12)
    p2 = 1
    r2 = 0
    for y in b[::-1]:
        p1 = 1
        r1 = 0
        for x in a[::-1]:
            r1 += p1 * int(x) * int(y)
            p1 *= 10
        r2 += p2 * r1
        print("{:>10} +".format(p2*r1))
        p2 *= 10
    print("-" * 12)
    print("{:>10}".format(r2))
    print("-" * 12)


if __name__ == '__main__':
    multiply("1234", "3456")
