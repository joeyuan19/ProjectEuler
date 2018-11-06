
def solve():
    with open('matrix.txt','r') as f:
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

#maze = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
#sol = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    I = len(maze)
    J = len(maze[0])

    #print J, I

    sol[0][0] = maze[0][0]

    for i in range(I):
            for j in range(J):
                    if i != I - 1:
                            if sol[i+1][j] == 0:
                                    sol[i+1][j] = sol[i][j] + maze[i+1][j]
                            else:
                                    if sol[i][j] + maze[i+1][j] < sol[i+1][j]:
                                            sol[i+1][j] = sol[i][j] + maze[i+1][j]
                    if j != J - 1:
                            if sol[i][j+1] == 0:
                                    sol[i][j+1] = sol[i][j] + maze[i][j+1]
                            else:
                                    if sol[i][j] + maze[i][j+1] < sol[i][j+1]:
                                            sol[i][j+1] = sol[i][j] + maze[i][j+1]
    return sol[-1][-1]

from timer import time_function
print(time_function(solve))
