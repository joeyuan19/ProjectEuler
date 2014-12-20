test = False 

def printMaze(x):
	I = len(x)
	J = len(x[0])
	for i in range(I):
		for j in range(J):
			print x[i][j],
		print
	print

if not test:
	with open('files/matrix2.txt','r') as f:
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

I = len(maze)
J = len(maze[0])

print J, I

for k in range(1):
	for j in range(J):
		for i in range(I):
			if j == 0:
				sol[i][j] = maze[i][j]
			else:
				sol[i][j] = maze[i][j] + sol[i][j-1]
		for i in range(I):
			if i != 0:
				if sol[i][j] > maze[i][j] + sol[i-1][j]:
					sol[i][j] = maze[i][j] + sol[i-1][j]
			if i != I - 1:
				if sol[i][j] > maze[i][j] + sol[i+1][j]:
					sol[i][j] = maze[i][j] + sol[i+1][j]
		for i in range(I-1,-1,-1):
			if i != 0:
				if sol[i][j] > maze[i][j] + sol[i-1][j]:
					sol[i][j] = maze[i][j] + sol[i-1][j]
			if i != I - 1:
				if sol[i][j] > maze[i][j] + sol[i+1][j]:
					sol[i][j] = maze[i][j] + sol[i+1][j]


min = sol[0][J-1]


for i in range(I):
	if min > sol[i][J-1]:
		min = sol[i][J-1]

print min


