
cubes = []

for i in xrange(10000):
    cubes.append(i**3)

matches = {}
for cube in cubes:
    s = ''.join(i for i in sorted(str(cube)))
    if s not in matches:
        matches[s] = [cube]
    else:
        matches[s].append(cube)

for match in matches:
    if len(matches[match]) == 5:
        print min(i for i in matches[match])

