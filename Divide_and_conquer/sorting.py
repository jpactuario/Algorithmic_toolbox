# Use Python2

import random

def partition3(a, l, r):
    x = a[l]
    j1 = l;
    j2 = l;
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j1 += 1
            j2 += 1
            a[i], a[j1] = a[j1], a[i]
            if j2 > j1:
                a[i],a[j2] = a[j2],a[i]
        elif a[i] == x:
            j2 += 1
            a[i], a[j2] = a[j2], a[i]
    a[l], a[j1] = a[j1], a[l]
    return j1, j2

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1,m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);

import sys
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, a = data[0], data[1:]
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print x,
