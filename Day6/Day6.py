with open("Day6/Day6Inputs.txt", 'r') as f:
    lanternFishDays = [int(number) for number in f.readline().split(',')]

FishDays = [0] * 9
for fish in lanternFishDays:
    FishDays[fish] += 1

for i in range(0, 256):
    today = i % len(FishDays)
    FishDays[(today + 7) % len(FishDays)] += FishDays[today]

print(sum(FishDays))