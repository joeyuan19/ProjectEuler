from totient import totients

def coprimes(L,report_progress=False):
    if report_progress:
        t = sum(totients(L))
        itr = 0.
    for d,n in ((2,1),(3,1)):
        for i,j in _coprimes(d,n,L,report_progress):
            if report_progress:
                print str(100*itr/t)[:5]+"%"," "*20,"\r",
                itr += 1
            yield i,j
    if report_progress:
        print

def _coprimes(d,n,L,report_progress=False):
    q = [(d,n)]
    quit = 0
    while len(q) > 0:
        quit += 1
        nxt = q.pop()
        if nxt[1] >= L or nxt[0] > L or nxt[1] > nxt[0]:
            continue
        else:
            yield nxt
            q.append((2*nxt[0]-nxt[1],nxt[0]))
            q.append((2*nxt[0]+nxt[1],nxt[0]))
            q.append((nxt[0]+2*nxt[1],nxt[1]))
