"""N-th element in fibonacci series."""
# some use seed as 0,1 or 1, 1
SEED = 0, 1,

def fibonacci1(n):
    """simple recursive approach."""
    if n > 1:
        print("compute: {}".format(n))
        return fibonacci1(n-2) + fibonacci1(n - 1)
    else:
        return n


def fibonacci2(n):
    """memorized dynamic programming approach."""
    # since this is a series of size N, we could just use array instead of dict.
    cache = [None] * (n+1)
    def compute(i):
        result = cache[i]
        if result is None:
            print("compute: {}".format(i))
            if i > 1: 
                result = compute(i-2) + compute(i-1)
            else:
                result = SEED[i]
            cache[i] = result
        return result
    return compute(n)

def fibonacci(n):
    """iterative approach."""
    buffer_ = SEED
    result = 0
    
    if n > 1:
        # f(0), f(1), f(2), ... f(n)
        for i in range(2, n + 1):
            result = buffer_[0] + buffer_[1]
            buffer_ = buffer_[1], result
    else:
        result = n    

    return result   
    

if __name__ == '__main__':
    print(fibonacci1(10))
    print("...")
    print(fibonacci2(10))
    print("...")
    print(fibonacci(10))
