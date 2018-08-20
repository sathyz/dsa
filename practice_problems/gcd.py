"""GCD of two numbers."""

def gcd(a, b):
    if b == 0:
        return a
    else:
        a_ = a % b
        return gcd(b, a_)


if __name__ == '__main__':
    print(gcd(357, 234))
    print(gcd(3918848, 1653264))
