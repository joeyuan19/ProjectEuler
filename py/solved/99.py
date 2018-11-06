from math import log


def convert(line):
    b,e = map(lambda x: int(x.strip()),line.split(','))
    return e*log(b)
def solve():
    m = -1
    ml = -1

    with open('99_base_exp.txt','r') as f:
        idx = 0
        for line in f:
            r = convert(line)
            if r > m:
                m = r
                ml = idx
            idx += 1

    return ml+1

from timer import time_function
print(time_function(solve))
        
