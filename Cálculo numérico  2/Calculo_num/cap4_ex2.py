from math import sin
from math import exp
from typing import Optional
import math
import numpy as np


def func(b, f=1000, L=0.1, R=1000):
    tan_t = (2 * np.pi * f * L) / R
    t = math.atan(tan_t)

    return sin(b - t) + sin(t) * exp(-b / ((2 * np.pi * f * L) / R))


def bisection_method(f, a, b, error_tol, max_iter=16) -> Optional[dict]:
    """
        Solves for an unknown root of a non-linear function, given the user inputed function, the
        initial upper and lower boundaries of the root, the maximum error tolerance desired and the
        number of iterations the algorithm will be perfomed.
    Args:
        f : The user defined function
        a : The initial lower root boundary
        b : The initial upper root boundary
        error_tol : The maximum error desired by the user
        max_iter : Maximum number of iterations the method will run for. Defaults to 16.

    Returns:
        dict: A dictionary containing the half way point found using the algorithm and the number of
        iterations that were used to perform the calculations.
    """
    hp = (a + b) / 2

    if f(a) * f(b) > 0:
        return print(f'No function root was found between the interval {a} and {b}')

    c = 0
    error = abs(f(a) - f(b))

    while error > error_tol:
        if c > max_iter:
            return print(f'Maximum number of {max_iter} iterations exceeded.')

        hp = (a + b) / 2.0

        if f(hp) == 0:
            return {"hp": hp, "iteration": c}
        elif f(a) * f(hp) < 0:
            b = hp

            c += 1
        else:
            a = hp

        error = abs(f(b) - f(a))

    return {"hp": hp, "iteration": c}


result = bisection_method(func, 0, 5, 0.0001, 20)

print(f'Root is approximately {result["hp"]:.4f} with {result["iteration"]} iterations')
