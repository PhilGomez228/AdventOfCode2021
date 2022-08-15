import numpy as np
with open("Day11/Day11Inputs.txt", 'r') as f:
    inputs = [line.strip() for line in f.readlines()]
print(inputs)
grid = np.zeros((10, 10), dtype=int)
count = 0


for i in range(0, len(inputs)):
    grid[i] = [j for j in inputs[i]]

#Regressive function to add the numbers spreading out for the flashes    
def lightFlash():
    global count 
    for line in range(0, len(grid)):
        for number in range(0, len(grid[line])):
            if grid[line, number] > 9:
                grid[line, number] = 0
                count += 1
                if line - 1 >= 0 and number - 1 >= 0:
                    if grid[line - 1, number - 1] == 0:
                        grid[line - 1, number - 1] = 0
                    else:    
                        grid[line - 1, number - 1] += 1
                        if grid[line - 1, number - 1] > 9:
                            lightFlash()
                if line - 1 >= 0 and number + 1 < len(grid[line]):
                    if grid[line - 1, number + 1] == 0:
                        grid[line - 1, number + 1] = 0
                    else:    
                        grid[line - 1, number + 1] += 1
                        if grid[line - 1, number + 1] > 9:
                            lightFlash()
                if line + 1 < len(grid) and number + 1 < len(grid[line]):
                    if grid[line + 1, number + 1] == 0:
                        grid[line + 1, number + 1] = 0
                    else:    
                        grid[line + 1, number + 1] += 1
                        if grid[line + 1, number + 1] > 9:
                            lightFlash()
                if line + 1 < len(grid) and number - 1 >= 0:
                    if grid[line + 1, number - 1] == 0:
                        grid[line + 1, number - 1] = 0
                    else:    
                        grid[line + 1, number - 1] += 1
                        if grid[line + 1, number - 1] > 9:
                            lightFlash()
                if line - 1 >= 0:
                    if grid[line - 1, number] == 0:
                        grid[line - 1, number] = 0
                    else:    
                        grid[line - 1, number] += 1
                        if grid[line - 1, number] > 9:
                            lightFlash()
                if number - 1 >= 0:
                    if grid[line, number - 1] == 0:
                        grid[line, number - 1] = 0
                    else:    
                        grid[line, number - 1] += 1
                        if grid[line, number - 1] > 9:
                            lightFlash()
                if line + 1 < len(grid):
                    if grid[line + 1, number] == 0:
                        grid[line + 1, number] = 0
                    else:    
                        grid[line + 1, number] += 1
                        if grid[line + 1, number] > 9:
                            lightFlash()
                if number + 1 < len(grid[line]):
                    if grid[line, number + 1] == 0:
                        grid[line, number + 1] = 0
                    else:    
                        grid[line, number + 1] += 1
                        if grid[line, number + 1] > 9:
                            lightFlash()
    return


print("Step 0", grid)
#For loop for part 1
#for i in range(0, 100):
#    grid += 1
#    if np.any(grid >= 10):
#        lightFlash()
#
#    print(f"Step {i + 1} \n", grid)
#    print(count)

#Loop converted to while loop for part 2
checkIfAllFlashed = True
step = 0
while checkIfAllFlashed:
    
    if np.all(grid == 0):
        print(step)
        checkIfAllFlashed = False
        break
    grid += 1
    if np.any(grid >= 10):
        lightFlash()

    print(f"Step {step} \n", grid)
    print(count)
    step += 1