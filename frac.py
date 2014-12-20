def round(n,dig):
    return int(n*10**dig)*10**-dig 



seq = []
N = 14
D = N**.5
itr = 1
while True:
    print D
    seq.append(round(D,5))
    D = 1/(D-int(D))
    if D in seq or itr > 20:
        print len(seq)-seq.index(D)
        break
    itr += 1

