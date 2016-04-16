# Use Python2

def get_majority_element(a,n):
    if n == 1: return 1
    a.sort()
    t = (n // 2) + 1
    count = 1
    for i in range(1,len(a)):
        if a[i] == a[i-1]:
            count += 1
        else:
            count = 1
        if count >= t:
            return 1
    return 0

import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, a = data[0],data[1:]
    print get_majority_element(a,n)