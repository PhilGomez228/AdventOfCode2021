with open("Day10/Day10Inputs.txt",'r') as f:
    inputs = [lines.strip() for lines in f.readlines()]

totalPoints = 0
incomplete = []
bracketsDictionary = {'(': ')', '[': ']', '{': '}', '<': '>'}
pointsDictionary = {')': 3, ']': 57, '}': 1197, '>': 25137}
for i in inputs:
    openBrackets = []
    
    for j in i:
        
        if j in bracketsDictionary.keys():
            openBrackets.append(j)
        if j == ')' or j == ']' or j == '}' or j == '>':
            if (bracketsDictionary[openBrackets[-1]] == j):
                    openBrackets.pop()
            else:
                totalPoints += pointsDictionary[j]
                openBrackets.clear()
                break
    if openBrackets not in incomplete:
        incomplete.append(openBrackets)
                

print("Part 1:", totalPoints)

#part 2
incomplete = [i for i in incomplete if i]

part2Points = []
for i in incomplete:
    linePoints = 0
    while(i):
        if i[-1] == '(':
            linePoints = linePoints * 5 + 1
        if i[-1] == '[':
            linePoints = linePoints * 5 + 2
        if i[-1] == '{':
            linePoints = linePoints * 5 + 3
        if i[-1] == '<':
                linePoints = linePoints * 5 + 4
        i.pop()
    part2Points.append(linePoints)
    
part2Points.sort()
print("part 2:", part2Points[len(part2Points) // 2])