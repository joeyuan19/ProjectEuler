
def solve():
    cubes = []

    for i in range(10000):
        cubes.append(i**3)

    matches = {}
    for cube in cubes:
        s = ''.join(i for i in sorted(str(cube)))
        if s not in matches:
            matches[s] = [cube]
        else:
            matches[s].append(cube)


    return min(min(matches[match]) for match in matches if len(matches[match]) == 5)

from timer import time_function
print(time_function(solve))
