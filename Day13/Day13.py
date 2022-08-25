import re
from collections import defaultdict
import numpy as np

with open("Day13/Day13Inputs.txt", 'r') as f:
    xyreg = [re.match(r"(?P<x>\d{1,}),(?P<y>\d{1,})", line) for line in f.readlines() if re.match(r"(?P<x>\d{1,}),(?P<y>\d{1,})", line) is not None] 
    
with open("Day13/Day13Inputs.txt", 'r') as f:  
    flipreg = [re.match(r"fold along (?P<fold>[x,y])=(?P<value>\d{1,})", line) for line in f.readlines()[len(xyreg) + 1:]]

x = []
y = []
flip = defaultdict(list)
for i in range(0, len(xyreg)):
    x.append(int(xyreg[i].group(1)))
    y.append(int(xyreg[i].group(2)))
    

grid = np.zeros((max(y) + 1, max(x) + 1))  
print(grid)  
for i in range(0, len(flipreg)):
    flip[flipreg[i].group(1)].append(int(flipreg[i].group(2)))
for i in range(0, len(xyreg)):
    grid[y,x] = 1

count = 0
for i in flip.keys():
    for j in flip[i]:
        if i == 'y':
            tempGrid = np.flipud(grid)
            tempGrid = np.delete(tempGrid, np.s_[j:], axis=0)
            grid = np.delete(grid, np.s_[j:], axis=0)
            grid += tempGrid
            count += 1
        elif i == 'x':
            tempGrid = np.fliplr(grid)
            tempGrid = np.delete(tempGrid, np.s_[j:], axis=1)
            grid = np.delete(grid, np.s_[j:], axis=1)
            grid += tempGrid
            count += 1
        if count <= 1:
            print(grid)
            print("Part 1:", np.count_nonzero(grid))

grid = grid > 0
grid = grid.astype(int)

print("Part 2:\n", grid)