def f(x, C):
    return x**2 + x**0.5 - C

def df(x):
    return 2*x + 0.5*x**-0.5

def solve(C, x=1.0, precision=1e-6):
    while abs(f(x, C)) > precision:
        x = x - f(x, C) / df(x)

    return x

print(f"{solve(float(input())):.6f}")
