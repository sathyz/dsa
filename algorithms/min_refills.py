"""Minimum number of refills required by car to reach the destination."""
def min_refills(x, L):
    """
    x => distance of gas station from origin (start).
    L => distance the car can run if tank is full.
    """
    num_refills = 0
    current_refill = 0
    n = len(x) - 2
    print(x[current_refill])
    while current_refill < n:
        last_refill = current_refill
        while (current_refill < n
                and x[current_refill + 1] - x[last_refill] <= L):
            current_refill += 1
        if current_refill == last_refill:
            raise Exception("Impossible")
        if current_refill <= n:
            print(x[current_refill])
            num_refills += 1
    return num_refills


if __name__ == '__main__':
    refills = min_refills([0, 200, 350, 500, 700, 900], 400)
    print(refills)
