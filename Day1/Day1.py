with open("Day1/Day1Entries.txt", 'r') as file:
    lines = file.readlines()
    depthInputs = [int(inputs.strip()) for inputs in lines]

count = 1
sumOfFirstGroupInputs = 0
numberDepthIncrease = 0
numberDepthDecrease = 0
#Count every 3 depth entries to sum, resetting back to 2 after comparing the 2 sums. 
#This is to account for the 2 depth entries in the previous sliding window to be included in the next sliding window.
for i in range(0, len(depthInputs)):
    #Once the count reaches 3, sum the sliding window and compare to the previous sliding window.
    if count == 3:
        sumOfSecondGroupInputs = depthInputs[i] + depthInputs[i - 1] + depthInputs[i - 2]
        if sumOfFirstGroupInputs == 0:
            count = 2      

        elif sumOfFirstGroupInputs < sumOfSecondGroupInputs:
            numberDepthIncrease += 1
            count = 2

        elif sumOfFirstGroupInputs > sumOfSecondGroupInputs:
            numberDepthDecrease += 1
            count = 2

        elif sumOfFirstGroupInputs == sumOfSecondGroupInputs:
            count = 2

        sumOfFirstGroupInputs = sumOfSecondGroupInputs

    count += 1

print("Number of depth entries that increased: " + str(numberDepthIncrease))