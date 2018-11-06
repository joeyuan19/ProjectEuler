import itertools

def read_connections(fname):
    data = []
    with open(fname,'r') as f:
        for line in f:
            data.append([-1 if i == '-' else int(i) for i in line.strip().split(',')])
    connections = []
    N = len(data)
    for r in range(N):
        for c in range(r+1,N):
            if data[r][c] > -1:
                connections.append((r,c,data[r][c]))
    return N,connections

def fully_connected(n_vertices,connections):
    return len(_fully_connected(0,connections,[])) == n_vertices

def weight(conns):
    return sum(i[2] for i in conns)

def _fully_connected(node,connections,in_graph):
    in_graph.append(node)
    for connection in connections:
        if node == connection[0] and connection[1] not in in_graph:
            for _node in _fully_connected(connection[1],connections,in_graph):
                if _node not in in_graph: 
                    in_graph.append(_node)
    return in_graph    

def solve(fname):
    v,c = read_connections(fname)
    c = sorted(c,key=lambda x:x[2])
    from math import factorial as f
    n = len(c)
    print(f(n)/f(n-v+1)/f(v-1))
    for subset in itertools.combinations(c,v-1):
        if fully_connected(v,subset):
            return weight(c)-weight(subset)

print(solve('files/p107_network.txt'))
