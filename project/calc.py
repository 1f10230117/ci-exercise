def fact(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def gcd(a, b):
    if b == 0:
        if a <= 0:
            return a * -1
        else:
            return a
    elif a == 0:
        if b <= 0:
            return b * -1
        else:
            return b
    else:
        return gcd(b, a % b)
    