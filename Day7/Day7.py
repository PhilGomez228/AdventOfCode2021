import numpy as np
with open("Day7/Day7Inputs.txt", 'r') as f:
    day7Inputs = [int(number) for number in f.readline().split(',')]

minFuel = []

maxInput = max(day7Inputs)
minInput = min(day7Inputs)
allDifferences = np.zeros((maxInput, len(day7Inputs)))

rangeNumber = maxInput - minInput
for i in range(minInput, maxInput):
    increment = 0
    allDifferences[i] = [(abs(day7Inputs[number] - i)) * (abs(day7Inputs[number] - i) + 1) // 2 for number in range(0, len(day7Inputs))]
    
    increment += 1
sumOfDifferences = []

for i in range(0, len(allDifferences[0])):
    sumOfDifferences.append(int(sum(allDifferences[i])))
    


print(min(sumOfDifferences))