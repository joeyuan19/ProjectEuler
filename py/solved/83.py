import math

test = True 

def printMaze(x):
	I = len(x)
	J = len(x[0])
	padding = -1
	for i in range(I):
		for j in range(J):
			if padding < 0:
				padding = int(math.log10(x[i][j]))
	for i in range(I):
		for j in range(J):
                        pass
			#print x[i][j],
		#print
	#print

if not test:
	with open('../files/matrix3.txt','r') as f:
		file = [line.strip() for line in f]

	maze = []
	sol = []

	for i in file:
		index = 0
		temp = []
		for j in range(len(i)):
			if i[j] == ",":
				temp.append(i[index:j])
				index = j + 1
		temp.append(i[index:])
		maze.append([int(k) for k in temp])
		sol.append([0 for k in range(len(temp))])
else:
	maze = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
	sol = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def solve():
    I = len(maze)
    J = len(maze[0])

    #print J, I

    last = -1
    t_last = -1

    temp = -1

    i = 0
    j = 0

    t_i = i
    t_j = j

    sol = maze[i][j]

    for i in range(20):
            for j in range(20):
                    pass
                    #print maze[i][j],
            #print
    #print

    i = 0
    j = 0


    for k in range(30):
#while i != I-1 or j != J-1:
            if i != 0 and last != 1: 
                    temp = maze[i-1][j]
                    t_last = 0
                    t_i = i-1
                    t_j = j
            if i != I - 1 and last != 0:	
                    if temp < 0:
                            temp = maze[i+1][j]
                            t_last = 1
                            t_i = i+1
                            t_j = j
                    elif temp > maze[i+1][j]:
                            temp = maze[i+1][j]
                            t_last = 1
                            t_i = i+1
                            t_j = j
            if j != 0 and last != 3:
                    if temp < 0:
                            temp = maze[i][j-1]	
                            t_last = 2
                            t_i = i
                            t_j = j-1
                    elif temp > maze[j-1][i]:
                            temp = maze[i][j-1]
                            t_last = 2
                            t_i = i
                            t_j = j-1
            if j != J - 1 and last != 2:
                    if temp < 0:
                            temp = maze[i][j+1] 
                            t_last = 3
                            t_i = i
                            t_j = j+1
                    elif temp > maze[i][j+1]:
                            temp = maze[i][j+1]
                            t_last = 3
                            t_i = i
                            t_j = j+1
            #print "(",i,",",j,") -> (",t_i,",",t_j,")" 
            i = t_i
            j = t_j
            t_i = -1
            t_j = -1
            last = t_last
            sol += temp
            temp = -1

    return sol


from timer import time_function
print(time_function(solve))
