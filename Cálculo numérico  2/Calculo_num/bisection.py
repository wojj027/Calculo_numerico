import math
from typing import Optional


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


if result := bisection_method(test_func, 2, 2.5, 0.0001, max_iter=20):
    print(f'Root is approximately {result["hp"]:.4f} with {result["iteration"]} iterations')
