#!/usr/bin/python3
def magic_calculation(a, b):
    answer = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            else:
                answer += a ** b / j
        except Exception:
            answer = b + a
            break
    return (answer)
