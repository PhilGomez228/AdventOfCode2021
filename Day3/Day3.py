with open("Day3/Day3Inputs.txt", 'r') as f:
    lines = f.readlines()
    binaryInputs = [inputs.strip("\n") for inputs in lines]


oxygenGeneratorRating = list(binaryInputs)
co2ScrubberRating = list(binaryInputs)
for i in range(0, len(binaryInputs[0])):
    if len(oxygenGeneratorRating) == 1:
        break
    inputsOfbinaryInPosition = [ binary[i] for binary in oxygenGeneratorRating]
    

    if inputsOfbinaryInPosition.count('1') >= inputsOfbinaryInPosition.count('0'):
        
        for rating in list(oxygenGeneratorRating):
            if rating[i] == '0':    
                oxygenGeneratorRating.remove(rating)
    else:
        for rating in list(oxygenGeneratorRating):
            if rating[i] == '1':
                oxygenGeneratorRating.remove(rating)
for i in range(0, len(binaryInputs[0])):
    if len(co2ScrubberRating) == 1:
        break
    inputsOfbinaryInPosition = [ binary[i] for binary in co2ScrubberRating]
    
    
    if inputsOfbinaryInPosition.count('1') < inputsOfbinaryInPosition.count('0'):
        for rating in list(co2ScrubberRating):
            if rating[i] == '0':
                co2ScrubberRating.remove(rating)
    else:
        for rating in list(co2ScrubberRating):
            if rating[i] == '1':
                co2ScrubberRating.remove(rating)

print('The oxygen generating rating is: ' + str(int(oxygenGeneratorRating[0], 2)))
print('The CO2 scrubber rating is : ' + str(int(co2ScrubberRating[0], 2)))
print('The life support rating of the submarine is: ' + str(int(co2ScrubberRating[0], 2) * int(oxygenGeneratorRating[0], 2)))