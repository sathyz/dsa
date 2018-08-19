"""Place paranthesis in the expression such that the result is maximum."""
msg = "5 - 8 + 7 * 4 - 8 + 9"

d = ["5", "8", "7", "4", "8", "9"]
op = ["-", "+", "*", "-", "+"]

n = len(d)

M = [[0]*n for _ in range(n)]
m = [[0]*n for _ in range(n)]

for i in range(n):
    M[i][i] = d[i]
    m[i][i] = d[i]


def compute(d1, op, d2):
    fml = "{} {} {}".format(d1, op, d2)
    # print(fml)
    return eval(fml)


def MinAndMax(i, j):
    min_ = None
    max_ = None
    for k in range(i, j):
        a = compute(M[i][k], op[k], M[k+1][j])
        b = compute(M[i][k], op[k], m[k+1][j])
        c = compute(m[i][k], op[k], M[k+1][j])
        d = compute(m[i][k], op[k], m[k+1][j])
        if min_ is None:
            min_ = min(a, b, c, d)
            assert max_ is None
            max_ = max(a, b, c, d)
        else:
            min_ = min(min_, a, b, c, d)
            assert max_ is not None
            max_ = max(max_, a, b, c, d)
    return min_, max_

def pprint(arr):
    data = "\n".join([" ".join(map(lambda x: "{:3d}".format(int(x)), row)) for row in arr])
    print(data)

def paranthesis():
    global M, m
    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j)
            # print("({}, {}) => {} {}".format(i, j, m[i][j], M[i][j]))
    # pprint(M)


if __name__ == '__main__':
    paranthesis()
    print(M[0][n-1])
