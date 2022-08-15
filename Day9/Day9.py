import numpy as np
from scipy import ndimage
with open("Day9/Day9Inputs.txt", 'r') as f:
    inputs = [number.strip() for number in f.readlines()]

length = len(inputs)
width = len(inputs[0])
chart = np.zeros((length, width), dtype=int)

for i in range(0,len(inputs)):

    splitInputs = [number.split() for number in inputs[i]]
    for j in range(0, len(splitInputs)):
        chart[i, j] = int(splitInputs[j][0])


#part 1

lowPoints = []

for i in range(0, len(chart)):
    for j in range(0, len(chart[0])):
        adjacentNumbers = []

        if i - 1 >= 0:
            adjacentNumbers.append(chart[i - 1, j])
        if j - 1 >= 0:
            adjacentNumbers.append(chart[i, j - 1])
        if j + 1 < len(chart[0]):
            adjacentNumbers.append(chart[i, j + 1])
        if i + 1 < len(chart):
            adjacentNumbers.append(chart[i + 1, j])

        if chart[i, j] < min(adjacentNumbers):
            lowPoints.append(chart[i, j] + 1)

print("Part 1:", sum(lowPoints))

#part 2

basinsLabeled, numLabel = ndimage.label(chart < 9)
sizeArray = np.bincount(basinsLabeled.ravel())
top3Sizes = sorted(sizeArray[1:], reverse=True)[:3]
print("part 2:", np.prod(top3Sizes))