with open("Day8/day8Inputs.txt", 'r') as f:
    data = [inputs.strip() for inputs in f.readlines()]
    inputs = [string.split(' | ')[0].strip().split(' ')  for string in data]
    outputs = [string.split('|')[1].strip().split(' ')  for string in data]

totalArray = []
for i in range(0, len(data)):
    valueKey = {}
    for value in inputs[i]:
        if len(value) == 2:
            valueKey[1] = value
        if len(value) == 4:
            valueKey[4] = value
        if len(value) == 3:
            valueKey[7] = value
        if len(value) == 7:
            valueKey[8] = value

    for value in inputs[i]:
        if len(value) == 6:
            if set(valueKey[4]).issubset(value):
                valueKey[9] = value
            elif set(valueKey[1]).issubset(value):
                valueKey[0] = value
            else:
                valueKey[6] = value

    for value in inputs[i]:
        if len(value) == 5:
            if set(valueKey[7]).issubset(value):
                valueKey[3] = value
            elif set(value).issubset(valueKey[6]):
                valueKey[5] = value
            else:
                valueKey[2] = value
   
    numberArray = []
    for value in outputs[i]:
        for x in range(0,10):
            if set(valueKey[x]) == set(value):
                numberArray.append(x)
                
    totalArray.append(int("".join(map(str, numberArray))))
print(sum(totalArray))  