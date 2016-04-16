# Uses python2

def get_fibonacci_last_digit(n):
    f_prev = 1        # F(1)
    f_prev_prev = 0   # F(0)
    if n <= 1:
        return n
    for i in range(2,n+1):
        new_f = (f_prev + f_prev_prev) % 10
        f_prev_prev = f_prev
        f_prev = new_f
    return new_f

import sys
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
