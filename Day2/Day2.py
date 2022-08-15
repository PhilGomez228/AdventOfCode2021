#Read the lines to create an array. Then create an array of arrays by splitting the string.
with open("Day2/Day2Inputs.txt", 'r') as f:
    lines = f.readlines()
    depthDirections = [directions.strip("\n") for directions in lines]
    depthDirections = [directions.split() for directions in lines]

depth = 0
horizontalPosition = 0
aim = 0
#Converting the numbers from string to integers.
for i in range(0, len(depthDirections)):
    depthDirections[i][1] = int(depthDirections[i][1])
    #calculateing change in depth/
    if depthDirections[i][0] == 'forward':
        horizontalPosition += depthDirections[i][1]

        if aim == 0:
            continue

        if aim > 0:
            depth += depthDirections[i][1] * aim

        if aim < 0:
            depth += depthDirections[i][1] * aim
    #Adjusting aim.
    elif depthDirections[i][0] == 'down':
        aim += depthDirections[i][1]

    elif depthDirections[i][0] == 'up':
        aim -= depthDirections[i][1]

print(horizontalPosition * depth)