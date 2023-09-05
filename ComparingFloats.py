def comparing_floats(a: float, b: float, tol: float) -> bool:
    absolute = abs(a - b)
    print(f'{a} - {b} = {a - b}')
    return absolute < tol


first = 0.8
second = 0.1 + 0.7

print(comparing_floats(first, second, tol=1e-10))
