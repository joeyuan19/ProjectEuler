def time_function(f,*args):
    import time
    t = time.time()
    r = f(*args)
    return (r,time.time()-t)
