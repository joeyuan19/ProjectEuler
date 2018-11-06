import time
import random
import matplotlib.pyplot as plt

def int1(x):
    return x == int(x)

def int2(x):
    return x%1 == 0

def int3(x):
    return x//1 == x

R = 1000
x_data = []
y = [[],[],[]]
N_data = [10**i for i in range(4)]
a = [[[],[],[]],[[],[],[]]]
for N in N_data:
    print(N)
    for X in [[random.randint(1,10**8) for r in range(R)],[random.randint(1,10**8)+(.1+random.random()*.8) for r in range(R)]]:
        y[0].append([])
        y[1].append([])
        y[2].append([])
        x_data.append(X)
        for x in X:
            ti = time.time()
            for i in range(N):
                int1(x)
            tf = time.time()
            y[0][-1].append((tf-ti)/N)

            ti = time.time()
            for i in range(N):
                int2(x)
            tf = time.time()
            y[1][-1].append((tf-ti)/N)

            ti = time.time()
            for i in range(N):
                int3(x)
            tf = time.time()
            y[2][-1].append((tf-ti)/N)
    for i in range(3):
        a[0][i].append(sum(y[i][0])/len(y[i][0]))
        a[1][i].append(sum(y[i][0])/len(y[i][0]))




plt.figure(1)
ax11 = plt.subplot(211)
for i in range(3):
    ax11.plot(x_data[0],y[i][0],'o',label='int'+str(i+1))
ax11.legend()
ax11.set_title('True')
ax12 = plt.subplot(212)
for i in range(3):
    ax12.plot(x_data[1],y[i][1],'o',label='int'+str(i+1))
ax12.legend()
ax12.set_title('False')
plt.figure(2)
ax21 = plt.subplot(211)
for i in range(3):
    ax21.plot(N_data,a[0][i],'o',label='int'+str(i+1))
ax21.set_title('True')
ax22 = plt.subplot(212)
for i in range(3):
    ax22.plot(N_data,a[1][i],'o',label='int'+str(i+1))
ax22.set_title('False')
plt.show()


