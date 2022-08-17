from collections import defaultdict
from collections import Counter

with open("Day12/Day12Inputs.txt", 'r') as f:
    inputs = [lines.strip().split('-') for lines in f.readlines()]


caveRoutes = defaultdict(set) 

for i in inputs:
    caveRoutes[i[0]].add(i[1])
    caveRoutes[i[1]].add(i[0])




fullPath = []
visited = set()
def dfsCaveMovement(routes, location, visited):
    if location == 'end':
        fullPath.append(routes)
    else:
        if location.islower():
            visited.add(location)
            
        for nextCave in caveRoutes[location]:
            if nextCave == 'start':
                continue
            elif nextCave == 'end' and nextCave not in routes:
                totalRoute = routes + [nextCave]
                dfsCaveMovement(totalRoute, nextCave, set(visited))
            elif nextCave.islower() and Counter(routes)[nextCave] < 2:
                for i in range(0, len(Counter(routes).most_common())):
                    if Counter(routes).most_common()[i][0].islower():
                        mostCommon = Counter(routes).most_common()[i][1]
                        break
                if Counter(routes)[nextCave] < 1:
                    totalRoute = routes + [nextCave]
                    dfsCaveMovement(totalRoute, nextCave, set(visited))
                elif mostCommon == 2:
                    continue
                else:
                    totalRoute = routes + [nextCave]
                    dfsCaveMovement(totalRoute, nextCave, set(visited))
            elif nextCave.isupper():
                totalRoute = routes + [nextCave]
                dfsCaveMovement(totalRoute, nextCave, set(visited))

dfsCaveMovement(['start'], 'start', visited)
print(fullPath)
print(len(fullPath))