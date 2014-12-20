from math import log


def convert(line):
    b,e = map(lambda x: int(x.strip()),line.split(','))
    return e*log(b)

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

print ml+1

    
