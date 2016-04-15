# Uses python2

from __future__ import division

def get_optimal_value(capacity, weights, values):
    value = 0
    for i in range(len(values)):
        if capacity == 0:
            return value
        # select item with highest values to weight ratio
        best = -1
        best_ratio = 0
        for j in range(len(values)):
            if weights[j] > 0:
                if values[j]/weights[j] > best_ratio:
                    best_ratio = values[j]/weights[j]
                    best = j
        if best == -1:    # no items left
            return value
        a = min(weights[best],capacity)
        value += values[best]*a/weights[best]
        capacity -= a
        weights[best] -= a
    return value

import sys

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))