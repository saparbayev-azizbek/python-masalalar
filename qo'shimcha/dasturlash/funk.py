def factorial(n):
    p = 1
    for i in range(1, n+1):
        p *= i
    return p

def prg(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s