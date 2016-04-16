# python2

def optimal_weight(W, w):
    n = len(w)
    value = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            value[i][j] = value[i-1][j]
            if w[i-1] <= j:
                val = value[i-1][j-w[i-1]] + w[i-1]
                if val > value[i][j]: value[i][j] = val
    return value[n][W]

import sys
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    W = data[0]
    n = data[1]
    w = data[2:]
    print optimal_weight(W, w)
