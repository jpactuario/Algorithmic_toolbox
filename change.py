# Uses python2

from __future__ import division

def get_change(n):
    i = 0
    while n // 10 > 0:
        i +=(n // 10)
        n = n % 10
    while n // 5 > 0:
        i +=(n // 5)
        n = n % 5
    i += n
    return i

import sys

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
