def time_function(f,*args,problem_number=None):
    import time
    t = time.time()
    r = f(*args)
    t = time.time()-t
    if problem_number is not None:
        try:
            with open('times.csv','r') as f:
                times = [line for line in f]
            with open('times.backup.csv','w') as f:
                f.write(''.join(times))
            while len(times) < problem_number:
                times.append('x\n')
            times[problem_number-1] = str(t)+'\n' 
            with open('times.csv','w') as f:
                f.write(''.join(times))
        except:
            pass
    return (r,t)
