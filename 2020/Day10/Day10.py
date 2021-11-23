# filename = 'test.txt'
# puzzleInput=[0]
filename = 'input.txt'
puzzleInput=[0]
with open(filename) as file:
  for line in file:
    puzzleInput.append(int(line.strip()))

puzzleInput.sort()
puzzleInput.append(puzzleInput[-1] + 3)
"""
oneDiffs = 0
threeDiffs = 0

for i in range( len( puzzleInput ) ):
  if i == len( puzzleInput) - 1 :
    continue
  else: diff = puzzleInput[ i+1 ] - puzzleInput[i]
  if diff == 1: oneDiffs += 1
  elif diff == 3: threeDiffs += 1


print(oneDiffs * threeDiffs)
"""
diffs = []
for i in range( len( puzzleInput ) ):
  if i == len( puzzleInput) - 1 :
    continue
  else: 
    diff = puzzleInput[ i+1 ] - puzzleInput[i]
    diffs.append(diff)

print(diffs)

oneCounts = []
count = 0
for i in range(len(diffs)):
  if diffs[i] == 1:
    count += 1
  if diffs[i] == 3:
    oneCounts.append(count)
    count = 0
print(oneCounts)
  
combos = []
for x in oneCounts:
  if x > 1:
    comb = 2**(x-1)
    if comb == 8: comb =7
    combos.append(comb)

print(combos)

total = 1 
for x in combos:
  total *= x

print(total)