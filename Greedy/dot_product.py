# Uses python2

def min_dot_product(a, b):
    res = 0
    while len(a) > 0:
        res += max(a) * min(b)
        a.remove(max(a))
        b.remove(min(b))
    return res

import sys
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
    
