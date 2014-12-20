

class SciNum(object):
    def __init__(self,base):
        self.exp = 0
        while abs(base) >= 10:
            base = base/10.
            self.exp += 1 
        self.base = base
        print self.base
        print self.exp
    
    def _raise(self,exp):
        self.base = self.base**exp
        self.exp = self.exp*exp

    def show(self):
        return str(self.base)+"x10^"+str(self.exp)

d = 23

for i in range(10):
    print d*i

