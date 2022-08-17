with open("Day10/Day10Inputs.txt",'r') as f:
    inputs = [lines.strip() for lines in f.readlines()]


CURVED = 3
SQUARE = 57
SQUIGGLY = 1197
CARROT = 25137

totalPoints = 0
incomplete = []
for i in inputs:
    openBrackets = []
    
    for j in i:
        
        if j == '(' or j == '[' or j == '{' or j == '<':
            openBrackets.append(j)
        if j == ')' or j == ']' or j == '}' or j == '>':
            if ((openBrackets[-1] == '(' and j == ')') or
                (openBrackets[-1] == '[' and j == ']') or
                (openBrackets[-1] == '{' and j == '}') or
                (openBrackets[-1] == '<' and j == '>')):
                    openBrackets.pop()
            else:
                if j == ')':
                    totalPoints += CURVED
                elif j == ']':
                    totalPoints += SQUARE
                elif j == '}':
                    totalPoints += SQUIGGLY
                elif j == '>':
                    totalPoints += CARROT
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