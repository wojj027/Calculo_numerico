from numpy import array, zeros


def gauss_elimination(A: array, b: array) -> None:  # cria-se a função do método
    """
        Performs the Gauss Elimination following two main steps:
        1 - Progressive elimination - The equations are handled to suppress one of the variables
                                      of the equations(scaling).
        2 - Regressive substitution - The last equation is solved directly and the result is
                                      regressively substituted on the equations before to determine
                                      the other variables.

    Args:
        A (array): A matrix representing the system's equations
        b (array): A matrix representing the system's equation results
    """

    n = len(b)
    x = zeros(n, float)

    # Progressive elimination step
    for k in range(n - 1):
        for i in range(k + 1, n):
            if A[i, k] == 0:
                continue
            fator = A[k, k] / A[i, k]
            for j in range(k, n):
                A[i, j] = A[k, j] - A[i, j] * fator
            b[i] = b[k] - b[i] * fator
    print(f'A =\n {A}')
    print(f'b =\n {b}')
    # Regressive substitution step
    x[n - 1] = b[n - 1] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += A[i, j] * x[j]
            x[i] = (b[i] - sum_ax) / A[i, i]
    f = 'System solution'
    print('-' * (len(f) + 32))
    print(f'{f:^50}')
    print('-' * (len(f) + 32))
    print(x)
    print('Where: ')
    for c in range(0, len(x)):
        print(f'\t x[{c}] = {x[c]} \n')


# Applying the method for the given exercise

A = array(
    [[6, -3, -3, 0, 0], [-3, 6, 0, -3, 0], [-3, 0, 6, -1, -2], [0, -3, -1, 5, 0], [0, 0, -2, 0, 3]]
)
b = array([0, 6, 0, 2, -3])
x = gauss_elimination(A, b)

# For this specific exercise and "A" and "b" matrixes, the result is all the values of x, which are
# x[0] = 4.0, x[1] = 5.0, x[2] = 3.0, x[3] = 4.0 and x[4] = 1.0
