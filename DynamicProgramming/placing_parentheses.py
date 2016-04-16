# python2

def evalt(i,j,m,M,op):
    maximum = -10**14
    minimum = +10**14
    for k in range(i,j):
        if op[k] == '+':
            if M[i][k] + M[k+1][j] > maximum:
                maximum = M[i][k] + M[k+1][j]
            if m[i][k] + m[k+1][j] < minimum:
                minimum = m[i][k] + m[k+1][j]
        elif op[k] == '-':
            if M[i][k] - m[k+1][j] > maximum:
                maximum = M[i][k] - m[k+1][j]
            if m[i][k] - M[k+1][j] < minimum:
                minimum = m[i][k] - M[k+1][j]            
        elif op[k] == '*':
            a = m[i][k] * m[k+1][j]
            b = m[i][k] * M[k+1][j]
            c = M[i][k] * m[k+1][j]
            d = M[i][k] * M[k+1][j]
            if max(a,b,c,d) > maximum:
                maximum = max(a,b,c,d)
            if min(a,b,c,d) < minimum:
                minimum = min(a,b,c,d)
        else:
            assert False
    return (minimum, maximum)

def get_maximum_value(data):
    d  = [int(k) for k in data[0::2]]
    op = [k for k in data[1::2]]
    n = len(d)
    m  = [[0 for k in range(n)] for k in range(n)]
    M  = [[0 for k in range(n)] for k in range(n)]
    for i in range(n):
        m[i][i], M[i][i] = d[i],d[i]
    for s in range(1,n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = evalt(i,j,m,M,op)   
    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(raw_input()))
