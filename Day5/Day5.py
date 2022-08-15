import numpy as np

with open("Day5/test.txt", "r") as f:
    day5Inputs = [line.strip() for line in f.readlines()]
splitCoordinates = [entry.split("->") for entry in day5Inputs]

separatedNumbers = []
for i in range(len(splitCoordinates)):
    for j in range(len(splitCoordinates[0])):
        separatedNumbers.append(splitCoordinates[i][j].split(","))

x1, y1, x2, y2 = [], [], [], []

for number in range(0, len(separatedNumbers)):
    if number % 2 == 0:
        x1.append(int(separatedNumbers[number][0]))
        y1.append(int(separatedNumbers[number][1]))
    else:
        x2.append(int(separatedNumbers[number][0]))
        y2.append(int(separatedNumbers[number][1]))

maxX = max(max(x1), max(x2))
maxY = max(max(y1), max(y2))
print(maxX, maxY)
diagram = np.zeros((maxX + 1, maxY + 1), dtype=int)

for i in range(0, len(splitCoordinates)):
    if x1[i] == x2[i]:
        for y in range(min(y1[i], y2[i]), max(y1[i], y2[i]) + 1):
            diagram[y, x1[i]] += 1
           
    elif y1[i] == y2[i]:
        for x in range(min(x1[i], x2[i]), max(x1[i], x2[i]) + 1):
            diagram[y1[i], x] += 1
    else:
        xDirection = 1 if x2[i] > x1[i]  else -1
        yDirection = 1 if y2[i] > y1[i]  else -1
        totalLine = max(abs(x1[i] - x2[i]), abs(y1[i] - y2[i]))
        for line in range(0, totalLine + 1):
            diagX = x1[i] + line * xDirection 
            diagY = y1[i] + line * yDirection
            diagram[diagY, diagX] += 1
          
print(diagram)
print("Score is ", (diagram >= 2).sum())