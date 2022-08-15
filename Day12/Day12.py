from collections import defaultdict

with open("Day12/test.txt", 'r') as f:
    inputs = [lines.strip().split('-') for lines in f.readlines()]
print(inputs)

caveRoutes = defaultdict(list) 

for i in inputs:
    caveRoutes[i[0]].append(i[1])
    caveRoutes[i[1]].append(i[0])
print(caveRoutes)

for i in caveRoutes:
    print(caveRoutes[i])