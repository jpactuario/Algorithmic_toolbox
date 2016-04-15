# Uses python2

import math

def optimal_summands(n):
    summands = []
    # Find minimum i such that i(i+1)/2 >= n
    # Solution is (sqrt(1+8*n)-1)/2, rounded up.
    i = (math.sqrt(1.0+8.0*n) - 1.0)/2.0
    j = math.ceil(i)
    for k in range(int(j)):
        summands.append(k+1)
    if i % 1 > 0.00000001:
        summands.remove(j*(j+1)/2 - n)
    return summands

import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print x,
