# python2

def lcs3(a, b, c):
    p = len(a)
    q = len(b)
    r = len(c)
    D = [[[0 for i in range(r+1)] for i in range(q+1)] for i in range(p+1)]
    for i in range(1,p+1):
        for j in range(1,q+1):
            for k in range(1,r+1):
                if a[i-1] == b[j-1] and b[j-1] == c[k-1]:
                    D[i][j][k] = max(D[i-1][j][k], D[i][j-1][k], D[i][j][k-1], D[i-1][j-1][k-1]+1)
                else:
                    D[i][j][k] = max(D[i-1][j][k], D[i][j-1][k], D[i][j][k-1])
    return D[p][q][r]

import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
