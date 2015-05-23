__author__ = 'jgibbs'


def fib(n):
    sequence = [0, 1]
    for i in range(3, n + 1):
        sequence.append(sequence[i-3] + sequence[i-2])

    return sequence