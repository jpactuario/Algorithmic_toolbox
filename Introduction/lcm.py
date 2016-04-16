# Uses python2

def lcm(a, b):
    return a * b / gcd(a,b)

def gcd(a, b):
    while a % b > 0:
        c = a % b
        a = b
        b = c
    return b

import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

