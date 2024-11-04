import math
from scipy.misc import derivative


# test function to avaluate if the algorithm works
def test_func(
    Id,
    n=2,
    k=1.3806 * (10 ** (-23)),
    V=24,
    T=300,
    q=1.6022 * (10 ** (-19)),
    Icr=31.9824 * (10 ** (-9)),
    R=10,
):
    return (n * (k * T / q)) * math.log((Id / Icr) + 1, math.e) + R * Id - V


def newton_raphson_method(f, x, error_tol, max_iter=16):
    a = f(x) / derivative(f, x)

    iter = 0

    while abs(a) > error_tol and iter < max_iter:
        if iter > max_iter:
            return print(f'Maximum number of {max_iter} iterations exceeded.')

        a = f(x) / derivative(f, x)

        x = x - a
        print(x)
        iter += 1
    return (x, iter)


x0 = 2
root, iter = newton_raphson_method(test_func, x0, 0.0001, 16)

print(f'Root is approximately {root:.5f} with {iter} iterations')
