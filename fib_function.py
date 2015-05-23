__author__ = 'jgibbs'


def fib(n):
    if n < 1:
        raise Exception("Invalid input: n must be >=1")
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(3, n + 1):
        sequence.append(sequence[i-3] + sequence[i-2])

    return sequence