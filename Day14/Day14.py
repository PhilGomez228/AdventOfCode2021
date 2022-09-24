from itertools import count

with open("Day14/Day14Inputs.txt",'r') as f:
    template = f.readline().strip()
    pairs = [pair.strip() for pair in f.readlines()[1:]]


pairDict = {}
for i in range(0, len(pairs)):
    pairDict[pairs[i].split(" -> ")[0]] = pairs[i].split(" -> ")[1]

#Day1    
#for j in range(0,10):

#     templatePairs = []
#     if j == 0:
#         for i in range(0, len(template)):
    
#             if i + 2 > len(template):
#                 break
#             else:
#                 templatePairs.append(template[i] + template[i+1])
            
#     else:
#         for i in range(0, len(newString)):
    
#             if i + 2 > len(newString):
#                 break
#             else:
#                 templatePairs.append(newString[i] + newString[i+1])
            
    
#     newString = templatePairs[0][0] + pairDict[templatePairs[0]] + templatePairs[0][1] 
#     for i in templatePairs[1:]:
#         newString = newString + pairDict[i] + i[1]
    
# print(len(newString))
# uniqueLetterString = set(newString)
# print(uniqueLetterString)
# countCharacters = {}
# for i in uniqueLetterString:
#     countCharacters[i] = newString.count(i)

# print(max(countCharacters.values()) - min(countCharacters.values()))

#Day2
pairCountDict = {}
pairCountDictAlternate = {}
letterCountDict = {}
pairSet = list(pairDict.keys())
pairSet = set("".join(pairSet))
for i in pairSet:
    letterCountDict[i] = 0

for i in pairDict.keys():
    pairCountDict[i] = 0
    pairCountDictAlternate[i] = 0

for i in range(0, len(template)):
    letterCountDict[template[i]] += 1
    if i + 2 > len(template):
                 break
    else:
        pairCountDict[template[i] + template[i+1]] += 1
        


for j in range(0,40):
    if any(value > 0 for value in pairCountDictAlternate.values()):
        for i in pairDict.keys():
                pairCountDict[i[0] + pairDict[i]] += pairCountDictAlternate[i]
                pairCountDict[pairDict[i] + i[1]] += pairCountDictAlternate[i]
                letterCountDict[pairDict[i]] += pairCountDictAlternate[i]
                pairCountDictAlternate[i] = 0
    elif any(value > 0 for value in pairCountDict.values()):
        for i in pairDict.keys():
                pairCountDictAlternate[i[0] + pairDict[i]] += pairCountDict[i]
                pairCountDictAlternate[pairDict[i] + i[1]] += pairCountDict[i]
                letterCountDict[pairDict[i]] += pairCountDict[i]
                pairCountDict[i] = 0

print(letterCountDict)
print(max(list(letterCountDict.values())) - min(list(letterCountDict.values())))